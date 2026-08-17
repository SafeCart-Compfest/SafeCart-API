# Repository strategy

`SafeCart-Compfest/SafeCart` is the only source of truth and the single repository link
for the preliminary submission. It contains the data contracts, AI experiments, runtime
API, future PWA, Docker Compose entrypoint, and technical documentation.

The older `SafeCart-API`, `SafeCart-PWA`, and `SafeCart-ScrapingData` repositories are
not runtime dependencies and must not receive parallel product development. They remain
untouched as historical references.

## Public boundary

This repository is public from its first project commit. Never commit credentials, raw
acquisition data, private screenshots, generated training pairs, model checkpoints, or
unlicensed content. Publish only source code, small synthetic fixtures, manifests,
checksums, aggregate metrics, and reviewed documentation.

## Evaluator path

The submitted commit must run from one clone with the root `compose.yaml`. External model
artifacts must be immutable, versioned, checksummed, and downloadable without private
credentials.

