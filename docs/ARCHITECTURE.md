# API service architecture

## Responsibility

`SafeCart-API` is the only backend exposed to `SafeCart-PWA`. It validates public
requests, calls private services, and maps their evidence into a stable response. It
does not load models or access raw BPOM snapshots.

```text
browser/PWA -> public API adapter -> orchestration -> AI gateway -> SafeCart-AI
```

Inbound FastAPI code and outbound HTTP clients depend on small application contracts.
No AI implementation is copied into this repository.

## Health contract

- `GET /health` is a liveness check and has no network dependency.
- `GET /ready` verifies the AI process contract and returns `503` when unavailable.

## Planned preliminary contract

The only product operation will be `POST /v1/assessments` with one in-memory PNG, JPEG,
or WebP upload of at most 10 MB. It will be added after AI acceptance, with explicit
`413`, `415`, `422`, and `503` errors. Clients will not supply official candidates.

No authentication, history, background jobs, crawler, distributed database, or
automatic takedown is in preliminary scope.
