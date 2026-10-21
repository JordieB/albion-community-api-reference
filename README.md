# Albion Online community API reference

This is an unofficial reference for an observed subset of Albion Online web APIs. The paths, query inputs, response status codes, and JSON shapes describe limited observations. They are not a complete server contract. A value shown as an example is not a required value, a supported range, or a promise that other combinations work.

Read the [API reference on GitHub](docs/reference/API.md) without installing anything. The [OpenAPI source](openapi/albion-community-api.yaml) is the single editable source for endpoint documentation. The `site/` directory contains the same reference in Swagger UI format for GitHub Pages or a local static preview. Request execution is disabled in that UI.

## Read and contribute

Each operation describes its path and inputs, observed example values where appropriate, sampled response status when recorded, and the sampled JSON shape. Generated response examples illustrate possible shapes; they are not captured response bodies. Unknown authentication behavior, query bounds, required query inputs, and response stability remain unverified.

To propose a correction, edit [the OpenAPI source](openapi/albion-community-api.yaml) in a pull request. Review the resulting generated Markdown and Swagger preview. Do not edit generated files directly.

## Rebuild locally

Node.js and a shell are needed only to regenerate the reference. Readers need neither. The build pins Widdershins 4.0.1 for Markdown and uses the vendored Swagger UI assets for the static site:

```sh
./scripts/build.sh
python3 -m unittest discover -s tests -v
```

To preview the static UI locally, serve this directory with any static-file server and open `site/`. For example, `python3 -m http.server 8000 --bind 127.0.0.1` serves it at `http://127.0.0.1:8000/site/`.

