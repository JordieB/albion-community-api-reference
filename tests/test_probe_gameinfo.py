"""Network-free tests for conservative live-probe behavior."""

import json
import base64
from pathlib import Path
import sys
import unittest
from urllib.error import URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import probe_gameinfo as probe


class ProbeTests(unittest.TestCase):
    def test_candidate_inventory_and_hosts(self):
        self.assertEqual(len(probe.CANDIDATES), 19)
        self.assertEqual(len({x[0] for x in probe.CANDIDATES}), 19)
        self.assertEqual(set(probe.HOSTS), {"americas", "europe", "asia"})

    def test_semantic_classification_rejects_catchall_and_empty(self):
        packed = lambda value: json.dumps(value).encode()
        self.assertEqual(probe.classify(200, "application/json", packed({"message": "OK"}), "guild")[0], "unconfirmed")
        self.assertEqual(probe.classify(200, "application/json", packed({"foo": "bar"}), "guild")[0], "unconfirmed")
        self.assertEqual(probe.classify(200, "application/json", packed([]), "events")[0], "limited_empty")
        self.assertEqual(probe.classify(404, "application/json", packed({"message": "no"}), "guild")[0], "unconfirmed")
        self.assertEqual(probe.classify(200, "text/html", b"<html/>", "guild")[0], "unconfirmed")
        self.assertEqual(probe.classify(200, "application/json", packed({"Id": "g1", "Name": "Guild"}), "guild")[0], "observed_populated")
        self.assertEqual(probe.classify(200, "application/json", packed({"Id": "g1", "message": "error"}), "guild")[0], "unconfirmed")
        self.assertEqual(probe.classify(200, "application/json", packed([{"Id": "p1", "error": "bad"}]), "members")[0], "unconfirmed")
        self.assertEqual(probe.classify(200, "application/json", packed({"guild": {"Id": "g1"}, "overall": {}}), "guild_data")[0], "observed_populated")
        event = [{"EventId": 1, "Killer": {"Id": "p1"}}]
        self.assertEqual(probe.classify(200, "application/json", packed(event), "events")[0], "observed_populated")
        png = b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\x0dIHDR" + (64).to_bytes(4, "big") + (64).to_bytes(4, "big")
        self.assertEqual(probe.classify(200, "image/png", png, "image")[0], "observed_image")
        self.assertEqual(probe.classify(200, "image/png", png[:12], "image")[0], "unconfirmed")
        self.assertEqual(probe.classify(200, "application/json", b"x" * (probe.MAX_BODY + 1), "events")[0], "unconfirmed")
        self.assertIsNone(probe.NoRedirect().redirect_request(None, None, 302, "Found", {}, "https://elsewhere.test"))

    def test_fresh_ids_region_scope_and_bounds(self):
        urls = []
        now = [0.0]

        def clock():
            return now[0]

        def sleep(seconds):
            now[0] += seconds

        def transport(url, timeout, cap):
            urls.append(url)
            self.assertEqual(timeout, 12)
            self.assertEqual(cap, probe.MAX_BODY)
            if "/events?" in url:
                value = [{"EventId": 99, "Killer": {"Id": "player1", "GuildId": "guild1"}}]
            elif "/battles?" in url:
                value = [{"id": 123, "totalFame": 1}]
            elif "/matches/crystal?" in url:
                value = [{"MatchId": 42, "StartTime": "now"}]
            elif "/guildmatches/top?" in url:
                value = [{"Id": 43, "StartTime": "now"}]
            elif "/__reference_probe_unknown_route__" in url:
                return 404, "application/json", b'{"message":"not found"}'
            else:
                value = []
            return 200, "application/json", json.dumps(value).encode()

        result = probe.Sampler("europe", transport=transport, clock=clock, sleep=sleep, utc=lambda: "2026-10-21T00:00:00+00:00").run()
        self.assertEqual(len(result["samples"]), 35)
        self.assertTrue(all("gameinfo-ams.albiononline.com" in url for url in urls))
        self.assertTrue(any("/players/player1/kills" in url for url in urls))
        self.assertTrue(any("/guilds/guild1/members" in url for url in urls))
        self.assertTrue(any("/battle/123" in url for url in urls))
        self.assertTrue(any("/matches/crystal/42" in url for url in urls))
        self.assertTrue(any("/guildmatches/43" in url for url in urls))
        self.assertGreaterEqual(now[0], len(urls) - 1)
        self.assertEqual(next(s for s in result["samples"] if s["label"] == "negative_control")["disposition"], "unconfirmed")
        self.assertTrue(result["negative_control_validated"])
        self.assertTrue(all(base64.b64decode(s["raw_base64"]) for s in result["samples"] if s["status"] is not None))

    def test_network_stop_preserves_all_candidate_dispositions(self):
        calls = []

        def failing(url, timeout, cap):
            calls.append(url)
            raise URLError("offline")

        result = probe.Sampler("asia", transport=failing, clock=lambda: 0, sleep=lambda _: None).run()
        self.assertEqual(len(calls), 2)
        self.assertEqual(sum(s["label"].startswith("candidate:") for s in result["samples"]), 19)
        self.assertTrue(all(s["disposition"] == "blocked" for s in result["samples"][2:]))

    def test_valid_control_and_event_battle_id(self):
        urls = []

        def transport(url, timeout, cap):
            urls.append(url)
            if "/__reference_probe_unknown_route__" in url:
                return 404, "application/json", b'{}'
            if "/events?" in url:
                return 200, "application/json", b'[{"EventId":1,"BattleId":42,"Victim":{"Id":"p1","GuildId":"g1"}}]'
            if "/battles?" in url:
                return 200, "application/json", b'[{"id":999,"totalFame":1}]'
            if "/guilds/g1/members" in url:
                return 200, "application/json", b'[{"Id":"p1","Name":"A"}]'
            return 200, "application/json", b'[]'

        result = probe.Sampler("europe", transport=transport, clock=lambda: 0, sleep=lambda _: None).run()
        self.assertTrue(result["negative_control_validated"])
        self.assertTrue(any("/battle/42?limit=1&offset=0" in url for url in urls))
        self.assertTrue(any("/players/p1/kills?limit=1&offset=0" in url for url in urls))
        self.assertTrue(any("/guilds/g1/top?range=week&limit=1&offset=0" in url for url in urls))
        self.assertEqual(next(s for s in result["samples"] if s["label"] == "candidate:/guilds/{id}/members")["disposition"], "observed_populated")

    def test_catchall_downgrades_candidate(self):
        def transport(url, timeout, cap):
            return 200, "application/json", b'[{"Id":"p1","Name":"A"}]'

        sampler = probe.Sampler("asia", transport=transport, clock=lambda: 0, sleep=lambda _: None)
        sampler.request("negative_control", "/__reference_probe_unknown_route__", "members")
        sample = sampler.request("candidate:/guilds/{id}/members", "/guilds/g1/members", "members")
        self.assertFalse(sampler.control_validated)
        self.assertEqual(sample["disposition"], "unconfirmed")
        self.assertIn("negative control", sample["reason"])
        variant = sampler.request("variant:test", "/players/statistics", "members")
        self.assertEqual(variant["disposition"], "unconfirmed")

    def test_rate_limit_stops_requests_and_statistics_scope(self):
        calls = []

        def transport(url, timeout, cap):
            calls.append(url)
            if "__reference_probe_unknown_route__" in url:
                return 404, "application/json", b'{}'
            return 429, "application/json", b'{"message":"limited"}'

        sampler = probe.Sampler("europe", transport=transport, clock=lambda: 0, sleep=lambda _: None)
        result = sampler.run("statistics")
        self.assertEqual(len(calls), 2)
        self.assertEqual(len(result["samples"]), 4)
        self.assertEqual([s["disposition"] for s in result["samples"]][2:], ["blocked", "blocked"])
        self.assertIn("Gathering:Fiber:Royal:week", result["samples"][1]["label"])
        self.assertNotIn("PvP", str(result))
        self.assertNotIn("solo", str(result))

    def test_nonpositive_event_battle_id_uses_battle_seed(self):
        urls = []

        def transport(url, timeout, cap):
            urls.append(url)
            if "/events?" in url:
                return 200, "application/json", b'[{"EventId":1,"BattleId":0,"Killer":{"Id":"p1"}}]'
            if "/battles?" in url:
                return 200, "application/json", b'[{"id":99,"totalFame":1}]'
            if "__reference_probe_unknown_route__" in url:
                return 404, "application/json", b'{}'
            return 200, "application/json", b'[]'

        probe.Sampler("europe", transport=transport, clock=lambda: 0, sleep=lambda _: None).run()
        self.assertTrue(any("/battle/99?limit=1&offset=0" in url for url in urls))
        self.assertFalse(any("/battle/0?" in url for url in urls))


if __name__ == "__main__":
    unittest.main()
