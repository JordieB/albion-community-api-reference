#!/usr/bin/env python3
"""Opt-in, bounded observations of proposed Albion Gameinfo routes.

This is a sampling tool, not a contract or an availability monitor. It makes GET
requests only when --run-live is supplied. Its transport and clock are injectable
so classification can be tested without network access.
"""

import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


HOSTS = {
    "americas": "gameinfo.albiononline.com",
    "europe": "gameinfo-ams.albiononline.com",
    "asia": "gameinfo-sgp.albiononline.com",
}
BASE = "/api/gameinfo"
MAX_BODY = 2 * 1024 * 1024
TIMEOUT = 12
MIN_INTERVAL = 1.0

# kind is deliberately conservative: an arbitrary JSON object is never enough.
CANDIDATES = (
    ("/players/{id}/kills", "events", "player"),
    ("/players/{id}/deaths", "events", "player"),
    ("/guilds/{id}/members", "members", "guild"),
    ("/guilds/{id}/data", "guild", "guild"),
    ("/guilds/{id}/top", "events", "guild"),
    ("/battle/{id}", "events", "battle"),
    ("/items/{id}", "image", "item"),
    ("/items/{id}/_itemCategoryTree", "category", "item"),
    ("/matches/crystal", "matches", None),
    ("/matches/crystal/{id}", "match", "crystal_match"),
    ("/guildmatches/top", "matches", None),
    ("/guildmatches/next", "matches", None),
    ("/guildmatches/past", "matches", None),
    ("/guildmatches/{id}", "match", "guild_match"),
    ("/events/playerfame", "ranking", None),
    ("/events/guildfame", "ranking", None),
    ("/events/playerweaponfame", "ranking", None),
    ("/guilds/topguildsbyattacks", "ranking", None),
    ("/guilds/topguildsbydefenses", "ranking", None),
)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def http_get(url, timeout=TIMEOUT, max_body=MAX_BODY):
    """Return (status, MIME, bytes); redirects are reported, never followed."""
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "albion-reference-observation/1"}, method="GET")
    try:
        response = build_opener(NoRedirect()).open(request, timeout=timeout)
    except HTTPError as exc:
        response = exc
    with response:
        mime = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        body = response.read(max_body + 1)
        return response.status, mime, body


def object_with_keys(value, keys):
    return isinstance(value, dict) and any(key in value and value[key] is not None for key in keys)


def meaningful(value, kind):
    if isinstance(value, dict) and any(k in value for k in ("error", "Error", "message", "Message", "status", "Status")):
        return False
    if kind == "events":
        return object_with_keys(value, ("EventId", "Killer", "Victim", "TotalVictimKillFame"))
    if kind == "members":
        return object_with_keys(value, ("Id", "Name", "GuildId"))
    if kind == "guild":
        return object_with_keys(value, ("Id", "Name", "AllianceId", "MemberCount"))
    if kind == "guild_data":
        return (isinstance(value, dict) and isinstance(value.get("guild"), dict)
                and object_with_keys(value["guild"], ("Id", "Name", "GuildId"))
                and any(key in value for key in ("basic", "overall", "topPlayers")))
    if kind == "battle":
        return object_with_keys(value, ("id", "Id", "startTime", "totalFame", "players", "guilds"))
    if kind == "item":
        return object_with_keys(value, ("UniqueName", "uniqueName", "ItemType", "LocalizedNames"))
    if kind == "category":
        return object_with_keys(value, ("UniqueName", "uniqueName", "Children", "children", "Items", "items", "name"))
    if kind == "match":
        return object_with_keys(value, ("id", "Id", "MatchId", "startTime", "StartTime", "guilds", "Guilds", "teams", "Teams"))
    if kind == "matches":
        return object_with_keys(value, ("id", "Id", "MatchId", "StartTime", "startTime", "Guilds", "guilds"))
    if kind == "ranking":
        return object_with_keys(value, ("Id", "id", "Name", "name", "Fame", "fame", "KillFame", "killFame", "GuildId", "PlayerId"))
    return False


def classify(status, mime, body, kind):
    """Return conservative (disposition, reason, small shape) for one response."""
    shape = {"bytes": len(body)}
    if len(body) > MAX_BODY:
        return "unconfirmed", f"response exceeded {MAX_BODY}-byte cap", shape
    if status != 200:
        return "unconfirmed", f"HTTP {status}; absence is not established", shape
    if kind == "image":
        if mime == "image/png" and len(body) >= 24 and body[:8] == b"\x89PNG\r\n\x1a\n" and body[12:16] == b"IHDR":
            width = int.from_bytes(body[16:20], "big")
            height = int.from_bytes(body[20:24], "big")
            if 0 < width <= 8192 and 0 < height <= 8192:
                shape.update(type="png", width=width, height=height)
                return "observed_image", "PNG signature and positive IHDR dimensions", shape
        return "unconfirmed", "response does not have valid PNG header and dimensions", shape
    if mime != "application/json" and not mime.endswith("+json"):
        return "unconfirmed", f"unexpected MIME {mime or '(none)'}", shape
    try:
        value = json.loads(body)
    except (ValueError, UnicodeDecodeError):
        return "unconfirmed", "invalid JSON", shape
    if isinstance(value, dict):
        shape["type"] = "object"
        shape["keys"] = sorted(value)[:16]
        if any(k in value for k in ("error", "Error", "message", "Message", "status", "Status")):
            return "unconfirmed", "error-like JSON object", shape
    elif isinstance(value, list):
        shape["type"] = "array"
        shape["length"] = len(value)
        if value and isinstance(value[0], dict):
            shape["item_keys"] = sorted(value[0])[:16]
    else:
        shape["type"] = type(value).__name__
    if isinstance(value, list) and not value:
        return "limited_empty", "empty JSON array; only status and top-level shape observed", shape
    if isinstance(value, dict) and not value:
        return "limited_empty", "empty JSON object; only status and top-level shape observed", shape
    if kind in ("events", "members", "matches", "ranking"):
        if isinstance(value, list) and all(meaningful(x, kind) for x in value):
            return "observed_populated", "populated JSON array with route-specific fields", shape
    elif kind == "category":
        if isinstance(value, (dict, list)) and (meaningful(value, kind) if isinstance(value, dict) else all(meaningful(x, kind) for x in value)):
            return "observed_populated", "populated category-like JSON", shape
    elif meaningful(value, kind):
        return "observed_populated", "populated JSON object with route-specific fields", shape
    return "unconfirmed", "JSON does not match conservative route shape", shape


def find_id(value, names):
    if isinstance(value, dict):
        for name in names:
            candidate = value.get(name)
            if isinstance(candidate, (str, int)) and not isinstance(candidate, bool) and str(candidate):
                return str(candidate)
        for nested in value.values():
            found = find_id(nested, names)
            if found:
                return found
    elif isinstance(value, list):
        for nested in value[:2]:
            found = find_id(nested, names)
            if found:
                return found
    return None


class Sampler:
    def __init__(self, region, transport=http_get, clock=time.monotonic, sleep=time.sleep, utc=None):
        self.region = region
        self.host = HOSTS[region]
        self.transport = transport
        self.clock = clock
        self.sleep = sleep
        self.utc = utc or (lambda: datetime.now(timezone.utc).isoformat())
        self.last_request = None
        self.network_failures = 0
        self.rate_limited = False
        self.samples = []
        self.payloads = {}
        self.control_validated = False

    def request(self, label, path, kind, query=None):
        if self.rate_limited:
            return self.blocked(label, path, "region stopped after HTTP 429", query)
        if self.network_failures >= 2:
            return self.blocked(label, path, "region stopped after two network failures", query)
        encoded = urlencode(query or {})
        url = f"https://{self.host}{BASE}{path}" + (f"?{encoded}" if encoded else "")
        assert urlsplit(url).hostname == self.host
        if self.last_request is not None:
            self.sleep(max(0.0, MIN_INTERVAL - (self.clock() - self.last_request)))
        self.last_request = self.clock()
        sample = {"label": label, "url": url, "utc": self.utc(), "status": None, "mime": None}
        try:
            status, mime, body = self.transport(url, TIMEOUT, MAX_BODY)
            sample.update(status=status, mime=mime)
            if status == 429:
                self.rate_limited = True
            disposition, reason, shape = classify(status, mime, body, kind)
            sample["raw_sha256"] = hashlib.sha256(body).hexdigest()
            sample["raw_base64"] = base64.b64encode(body).decode("ascii")
            if label == "negative_control":
                self.control_validated = status == 404
            elif label.startswith(("candidate:", "variant:")) and disposition in ("observed_populated", "observed_image", "limited_empty") and not self.control_validated:
                disposition, reason = "unconfirmed", "negative control not validated; route-specific observation cannot be distinguished from catch-all"
            sample.update(disposition=disposition, reason=reason, shape=shape)
            if disposition == "observed_populated":
                self.payloads[label] = json.loads(body)
        except (URLError, TimeoutError, OSError) as exc:
            self.network_failures += 1
            sample.update(disposition="unconfirmed", reason=f"network failure: {type(exc).__name__}")
        self.samples.append(sample)
        return sample

    def blocked(self, label, path, reason, query=None):
        encoded = urlencode(query or {})
        url = f"https://{self.host}{BASE}{path}" + (f"?{encoded}" if encoded else "")
        sample = {"label": label, "url": url, "utc": self.utc(), "status": None, "mime": None,
                  "disposition": "blocked", "reason": reason}
        self.samples.append(sample)
        return sample

    def run(self, scope="all"):
        if scope == "statistics":
            self.request("negative_control", "/__reference_probe_unknown_route__", "guild")
            self.statistics_matrix()
            return self.result()
        self.request("seed_events", "/events", "events", {"limit": 1, "offset": 0})
        self.request("seed_battles", "/battles", "matches", {"sort": "recent", "limit": 1, "offset": 0})
        event = self.payloads.get("seed_events")
        battle = self.payloads.get("seed_battles")
        event_battle_id = find_id(event, ("BattleId",)) if event else None
        if event_battle_id and (not event_battle_id.isdecimal() or int(event_battle_id) <= 0):
            event_battle_id = None
        ids = {"player": None,
               "guild": None,
               "battle": event_battle_id or (find_id(battle, ("id", "Id")) if battle else None),
               "item": "T4_BAG"}
        # Player ID must come specifically from Killer/Victim; never from EventId.
        if isinstance(event, list) and event and isinstance(event[0], dict):
            ids["player"] = find_id(event[0].get("Killer"), ("Id",)) or find_id(event[0].get("Victim"), ("Id",))
            ids["guild"] = find_id(event[0].get("Killer"), ("GuildId",)) or find_id(event[0].get("Victim"), ("GuildId",))
        self.request("negative_control", "/__reference_probe_unknown_route__", "guild")
        for path, kind, id_type in CANDIDATES:
            if id_type in ("crystal_match", "guild_match"):
                if id_type == "crystal_match":
                    ids[id_type] = find_id(self.payloads.get("candidate:/matches/crystal"), ("id", "Id", "MatchId"))
                else:
                    ids[id_type] = next((found for label in ("candidate:/guildmatches/top", "candidate:/guildmatches/next", "candidate:/guildmatches/past")
                                         if (found := find_id(self.payloads.get(label), ("id", "Id", "MatchId")))), None)
            label = f"candidate:{path}"
            identifier = ids.get(id_type) if id_type else None
            if id_type and not identifier:
                self.blocked(label, path, f"no fresh {id_type} ID from successful parent sample")
                continue
            actual = path.replace("{id}", quote(identifier, safe="")) if identifier else path
            query = {"limit": 1, "offset": 0} if kind in ("events", "members", "ranking", "matches") else None
            if path == "/events/playerweaponfame":
                query = {"weaponCategory": "all", "range": "week", "limit": 1, "offset": 0}
            if path in ("/events/playerfame", "/events/guildfame", "/guilds/topguildsbyattacks", "/guilds/topguildsbydefenses", "/guilds/{id}/top"):
                query = {"range": "week", "limit": 1, "offset": 0}
            if path in ("/players/{id}/kills", "/players/{id}/deaths", "/battle/{id}"):
                query = {"limit": 1, "offset": 0}
            if path == "/guilds/{id}/data":
                kind = "guild_data"
            self.request(label, actual, kind, query)
        for label, path, kind, variants in (
            ("battles_range", "/battles", "matches", ({"range": x, "sort": "recent", "limit": 1, "offset": 0} for x in ("day", "week", "month"))),
            ("battles_sort", "/battles", "matches", ({"sort": x, "limit": 1, "offset": 0} for x in ("totalFame", "totalKills"))),
            ("statistics_range", "/players/statistics", "ranking", ({"range": x, "limit": 1, "offset": 0} for x in ("day", "week", "month"))),
            ("killfame_range", "/events/killfame", "events", ({"range": x, "limit": 1, "offset": 0} for x in ("month", "lastMonth"))),
        ):
            for query in variants:
                self.request(f"variant:{label}:{next(iter(query.values()))}", path, kind, query)
        self.statistics_matrix()
        return self.result()

    def statistics_matrix(self):
        # Exact examples from the community note; the response cannot prove the
        # server used these inputs or establish all accepted values.
        for category, subtype, world, period in (
            ("Gathering", "Fiber", "Royal", "week"),
            ("Gathering", "Ore", "Outlands", "month"),
            ("PvE", "All", "Hellgate", "week"),
        ):
            self.request(f"variant:statistics:{category}:{subtype}:{world}:{period}", "/players/statistics", "ranking",
                         {"type": category, "subtype": subtype, "region": world,
                          "range": period, "limit": 1, "offset": 0})

    def result(self):
        return {"region": self.region, "host": self.host, "negative_control_validated": self.control_validated,
                "samples": self.samples,
                "note": "A populated sample confirms one observed response only; query acceptance, effect, bounds, stability, authentication, and other regions remain unverified."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-live", action="store_true", help="required to make network requests")
    parser.add_argument("--regions", nargs="+", choices=tuple(HOSTS), default=list(HOSTS))
    parser.add_argument("--scope", choices=("all", "statistics"), default="all", help="statistics samples only, with negative control")
    parser.add_argument("--output", type=Path, help="JSON evidence path; parent directory must exist")
    args = parser.parse_args(argv)
    if not args.run_live:
        parser.error("no requests made: supply --run-live to opt in")
    if not args.output:
        parser.error("--output is required")
    result = {"schema_version": 1, "generated_utc": datetime.now(timezone.utc).isoformat(),
              "method": f"GET, sequential, >=1s spacing, 12s timeout, {MAX_BODY}-byte response cap, no redirects or retries",
              "regions": [Sampler(region).run(args.scope) for region in args.regions]}
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} ({sum(len(r['samples']) for r in result['regions'])} samples)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
