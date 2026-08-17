# SafeCart API

Public gateway and orchestration service for SafeCart, an evidence-grounded marketplace
listing identity assessment system for COMPFEST 18 AIC.

SafeCart reports whether information visible in a listing is consistent with versioned
BPOM evidence. It does **not** determine physical authenticity, chemical safety, or
legal liability.

## Service boundary

This repository owns:

- the public HTTP contract consumed by `SafeCart-PWA`;
- upload validation, request limits, error mapping, and response schemas;
- synchronous orchestration of the private `SafeCart-AI` service;
- API health, dependency readiness, tests, and Docker image.

It does not contain OCR, matching, training, data acquisition, datasets, model weights,
frontend code, or the root Docker Compose file. Those belong to `SafeCart-AI`,
`SafeCart-ScrapingData`, `SafeCart-PWA`, and `SafeCart-Deployment` respectively.

## Current flow

```text
SafeCart-PWA -> SafeCart-API -> SafeCart-AI
```

The current bootstrap exposes process health and AI dependency readiness. The public
`POST /v1/assessments` endpoint will be implemented after the AI pipeline passes its
acceptance gate, so the competition contract is not prematurely coupled to a baseline.

## Local development

Requirements: Python 3.11-3.13 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --extra dev
uv run uvicorn safecart_api.main:app --reload --port 8000
```

Copy `.env.example` to `.env` only for local overrides. By default, the gateway expects
SafeCart AI at `http://localhost:8001`.

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ready
```

- `/health` reports API process liveness without touching dependencies.
- `/ready` returns `200` only when SafeCart AI responds with its expected health
  contract; otherwise it returns `503`.

## Validation

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy
uv run pytest --cov=safecart_api --cov-report=term-missing
docker build -t safecart-api .
```

Cross-service startup belongs in `SafeCart-Deployment`. See `CONTRIBUTING.md` for the
protected-branch workflow.
