# Albion Online community API reference

This is an unofficial reference for an observed subset of Albion Online web APIs. The paths, query inputs, response status codes, and JSON shapes describe limited observations. They are not a complete server contract. A value shown as an example is not a required value, a supported range, or a promise that other combinations work.

Read the [API reference on GitHub](docs/reference/API.md) without installing anything. The [OpenAPI source](openapi/albion-community-api.yaml) is the single editable source for endpoint documentation. The `site/` directory contains the same reference in Swagger UI format for GitHub Pages or a local static preview. Request execution is disabled in that UI.

## Read and contribute

Each operation describes its path and inputs, observed example values where appropriate, sampled response status when recorded, and the sampled JSON shape. Generated response examples illustrate possible shapes; they are not captured response bodies. Unknown authentication behavior, query bounds, required query inputs, and response stability remain unverified.

To propose a correction, edit [the OpenAPI source](openapi/albion-community-api.yaml) in a pull request. Review the resulting generated Markdown and Swagger preview. Do not edit generated files directly.

## Related community projects

Use this reference alongside the community's clients, data collectors, and catalogs. SBI Gameinfo provides player, guild, and combat information; the [Albion Online Data Project (AODP)](https://www.albion-online-data.com/) collects market and gold data from players. Static game dumps and independently hosted APIs serve different needs.

| Project | Useful for | Service or data source |
| --- | --- | --- |
| [simple-albion-api](https://github.com/SantiagoSaldana/simple-albion-api) | TypeScript/Node.js player, guild, event, and battle integrations, with Americas, Europe, and Asia selection. | SBI Gameinfo client. |
| [Albion Online API PHP client](https://github.com/ica4c/albion-online-api-php-client) | Adding player lookups, guild rosters, and combat reports to PHP applications. | Includes an SBI Gameinfo client. |
| [AODP PHP client](https://github.com/ica4c/albion-online-data-project-php-client) | Fetching item and gold prices for PHP market tools. | AODP client; separate from the Gameinfo PHP client above. |
| [albiondata-client](https://github.com/ao-data/albiondata-client) | Contributing market observations that power community price tools. | AODP network-traffic collection client; coverage depends on what players load in game. |
| [ao-bin-dumps](https://github.com/ao-data/ao-bin-dumps) | Looking up item definitions and world data to enrich an application. | Static game-file dumps, not live prices or player activity. |
| [albiondata-server-rails](https://github.com/ao-data/albiondata-server-rails) | Exploring AODP server implementation and contributing upstream. | Its README warns that it is unfinished and not ready for use. |
| [OpenAlbion/api](https://github.com/OpenAlbion/api) | Exploring a self-hostable Laravel data/API platform. | Independent third-party project, with its own setup and API surface. |

For another community perspective on Gameinfo, see [Tools4Albion's API notes](https://www.tools4albion.com/api_info.php). External clients and notes are useful starting points, not verification of endpoint behavior in this reference. Check each project's current documentation, region support, and license before adopting it. In particular, `ao-bin-dumps` does not include a repository license; public availability alone does not establish reuse terms for game data.

To help connect these efforts, propose related-project additions with a direct source link and a concrete use case. Send client-specific fixes to the upstream project and reference corrections here. AODP's [community contact links](https://www.albion-online-data.com/#contact-us) provide a place to meet other data-tool builders.

## Rebuild locally

Node.js and a shell are needed only to regenerate the reference. Readers need neither. The build pins Widdershins 4.0.1 for Markdown and uses the vendored Swagger UI assets for the static site:

```sh
./scripts/build.sh
python3 -m unittest discover -s tests -v
```

To preview the static UI locally, serve this directory with any static-file server and open `site/`. For example, `python3 -m http.server 8000 --bind 127.0.0.1` serves it at `http://127.0.0.1:8000/site/`.

## Sample proposed Gameinfo routes

`scripts/probe_gameinfo.py` is an optional live observation tool. It does not run during tests or the reference build. Run offline checks with `python3 -m unittest discover -s tests -v`. To sample all three Gameinfo regions, create a private evidence directory and explicitly opt in:

```sh
mkdir -p ../probe-results
python3 scripts/probe_gameinfo.py --run-live --regions americas europe asia --output ../probe-results/gameinfo.json
```

The sampler makes sequential GET requests to the exact selected hosts, waits at least one second between requests, uses a 12-second timeout and a 2 MiB response cap, follows no redirects, and makes no retries. It stops requesting a region after two network failures. The output records each sampled URL, UTC time, status, MIME type, bounded shape summary, disposition, and bounded raw response encoded as base64 with a SHA-256 digest for independent review. Keep this evidence outside the publishable release tree, as shown above. The script requires the output directory to exist.

For a smaller sample of three statistics combinations and the unknown-route control, use `--scope statistics --regions europe`. The full run samples documented examples of `type`, `subtype`, `region`, and `range`; a requested value appearing in a URL does not prove the server used it.

An `observed_populated` result means only that one request returned populated JSON with recognizable fields. An empty result records limited status and top-level shape evidence. HTTP errors, unexpected JSON, missing fresh IDs, or network failures leave the route unconfirmed; they do not establish absence. A 200 response to a query does not establish that the server honored that parameter, and sampled values do not establish bounds or stability. Results apply only to the sampled host, URL, and UTC date; authentication behavior and unsampled combinations remain unknown. Do not add a route to the OpenAPI reference solely because a third-party list names it.

