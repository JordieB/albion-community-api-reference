#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

mkdir -p docs/reference site
npx --yes widdershins@4.0.1 -c --omitHeader --summary \
  openapi/albion-community-api.yaml -o docs/reference/API.md
# Widdershins retains a Slate code-tab instruction even when -c omits samples.
python3 - <<'PY'
from pathlib import Path

path = Path("docs/reference/API.md")
text = path.read_text(encoding="utf-8")
text = text.replace(
    "> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.\n\n",
    "",
)
path.write_text(text, encoding="utf-8")
PY
cp openapi/albion-community-api.yaml site/openapi.yaml
