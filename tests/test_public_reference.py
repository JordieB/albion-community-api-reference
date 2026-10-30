"""Offline checks for the publishable API-reference tree."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicReferenceTests(unittest.TestCase):
    def test_release_tree_has_only_reference_and_build_files(self):
        allowed = {
            Path(".gitignore"), Path("README.md"), Path("openapi/albion-community-api.yaml"),
            Path("docs/reference/API.md"), Path("site/index.html"),
            Path("site/openapi.yaml"), Path("site/reference.css"),
            Path("site/reference.js"), Path("site/vendor/swagger-ui/LICENSE"),
            Path("site/vendor/swagger-ui/NOTICE"),
            Path("site/vendor/swagger-ui/swagger-ui.css"),
            Path("site/vendor/swagger-ui/swagger-ui-bundle.js"),
            Path("scripts/build.sh"), Path("tests/test_public_reference.py"),
            Path("openapitools.json"),
            Path(".github/workflows/validate-reference.yml"),
            Path(".github/workflows/pages.yml"),
        }
        actual = {
            p.relative_to(ROOT) for p in ROOT.rglob("*")
            if p.is_file() and not {".git", "__pycache__"}.intersection(p.relative_to(ROOT).parts)
        }
        self.assertEqual(actual, allowed)

    def test_templated_paths_and_clean_reference_metadata(self):
        for name in ("README.md", "openapi/albion-community-api.yaml", "docs/reference/API.md", "site/openapi.yaml"):
            path = ROOT / name
            value = path.read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"\b[a-fA-F0-9]{64}\b", value), path)
            self.assertIsNone(re.search(r"(?:/Users/|[A-Z]:\\Users\\)", value), path)
        spec = (ROOT / "openapi/albion-community-api.yaml").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"(?m)^\s+x-[A-Za-z0-9_-]+:", spec))
        path_lines = re.findall(r'^  "(/[^"\n]+)":$', spec, re.M)
        self.assertEqual(len(path_lines), 35)
        for route in path_lines:
            self.assertIsNone(re.search(r"/[0-9]{3,}(?:/|$)", route), route)
            self.assertIsNone(re.search(r"/[A-Za-z0-9_-]{20,}(?:/|$)", route), route)
        self.assertIn("/api/gameinfo/events/{eventId}", path_lines)
        self.assertIn("/api/gameinfo/events/{subjectId}/history/{otherSubjectId}", path_lines)

    def test_github_and_pages_reference_are_derived_from_one_source(self):
        source = (ROOT / "openapi/albion-community-api.yaml").read_bytes()
        self.assertEqual((ROOT / "site/openapi.yaml").read_bytes(), source)
        markdown = (ROOT / "docs/reference/API.md").read_text(encoding="utf-8")
        self.assertIn("`GET /api/gameinfo/events`", markdown)
        self.assertIn("`GET /api/gameinfo/events/{eventId}`", markdown)
        self.assertIn("response shapes", markdown)
        self.assertIn("Example responses", markdown)
        self.assertIn("https://gameinfo.albiononline.com", markdown)
        self.assertIn("https://albiononline.com", markdown)
        self.assertIn("GET https://gameinfo.albiononline.com/api/gameinfo/events/<eventId>", markdown)
        self.assertIn("GET https://albiononline.com/characterbuilder/api/builds/<buildId>", markdown)
        self.assertIn("hosted Swagger UI disables request execution", markdown)
        self.assertNotIn("curl -X GET", markdown)
        self.assertNotIn("No authorization required", markdown)
        self.assertNotIn("http://localhost", markdown)
        self.assertNotIn("Scroll down for code samples", markdown)
        self.assertIn("[API reference on GitHub](docs/reference/API.md)", (ROOT / "README.md").read_text())

    def test_pages_assets_resolve_and_live_requests_are_disabled(self):
        html = (ROOT / "site/index.html").read_text(encoding="utf-8")
        js = (ROOT / "site/reference.js").read_text(encoding="utf-8")
        for asset in ("vendor/swagger-ui/swagger-ui.css", "vendor/swagger-ui/swagger-ui-bundle.js", "reference.css", "reference.js", "openapi.yaml"):
            self.assertTrue((ROOT / "site" / asset).is_file(), asset)
            self.assertIn(asset, html if asset != "openapi.yaml" else html + js)
        for setting in ("supportedSubmitMethods: []", "tryItOutEnabled: false", "validatorUrl: null", "queryConfigEnabled: false", "persistAuthorization: false"):
            self.assertIn(setting, js)
        self.assertIn("target.href !== specUrl.href", js)
        self.assertIn("connect-src 'self'", html)
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("if: vars.PUBLISH_PAGES == 'true'", pages)
        self.assertIn("path: site", pages)


if __name__ == "__main__":
    unittest.main()
