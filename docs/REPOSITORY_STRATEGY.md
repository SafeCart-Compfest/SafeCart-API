# Repository strategy

SafeCart uses service-oriented repositories with a consistent `SafeCart-{Purpose}`
naming convention.

## Service ownership

- `SafeCart-API`: synchronous backend, model training and evaluation code, inference,
  evidence policy, model integration, API contract, and API Docker image.
- `SafeCart-PWA`: mobile-first frontend and PWA assets only.
- `SafeCart-ScrapingData`: acquisition experiments and source snapshot tooling only; it
  is not a runtime dependency.

Create another repository only when a component has an independently deployable runtime,
ownership boundary, and release lifecycle. If inference is separated from the API in a
future phase, the only acceptable service name is `SafeCart-AI`.

## Public boundary

Competition repositories are public. Never commit credentials, raw acquisition data,
private screenshots, generated training pairs, model checkpoints, or unlicensed content.
Publish only source code, small synthetic fixtures, manifests, checksums, aggregate
metrics, and reviewed documentation.

## Submission integration

`SafeCart-API` is the primary source-code link and owns the root Docker Compose contract.
Its README links the other service repositories and pins compatible release versions.
The evaluator path must never depend on `SafeCart-ScrapingData`; prepared catalog and
model artifacts are immutable and checksummed.

