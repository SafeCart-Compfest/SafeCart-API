# SafeCart API

SafeCart is an evidence-grounded product identity consistency system. It compares a
marketplace listing with official BPOM records and produces review evidence. It does
not determine physical authenticity, chemical safety, or legal liability.

This repository is the backend and AI-inference service for the COMPFEST 18 AIC
submission. It contains the synchronous API boundary, deterministic normalization, data
and evaluation pipelines, a rule-based baseline, and the future fine-tuned matcher and OCR
adapters. The baseline must not be presented as the final AI model.

## Current flow

```text
Structured listing identity
        -> official candidates
        -> rule-based baseline
        -> field evidence + review status
```

Target flow:

```text
Listing screenshot
        -> OCR + entity extraction
        -> BPOM candidate retrieval
        -> fine-tuned pair matcher
        -> calibrated evidence report
```

## Requirements

- Python 3.11-3.13 (3.12 recommended)
- [uv](https://docs.astral.sh/uv/)
- Docker with Compose for the evaluator path

## Local setup

```bash
uv sync --extra dev
uv run pytest
uv run uvicorn safecart.main:app --reload
```

Open `http://localhost:8000/docs` for the interactive API documentation.

## Docker setup

The compose file mounts the workspace-level `dataset/Data BPOM` directory read-only.

```bash
docker compose up --build
```

Verify:

```bash
curl http://localhost:8000/health
```

## Audit the BPOM snapshot

Run this before any training or evaluation:

```bash
uv run safecart-audit-bpom "../dataset/Data BPOM" --output outputs/bpom-audit.json
```

The audit reports missing fields and NIE values associated with multiple distinct
official identities. The downstream system must preserve those candidates and abstain
from automatic approval.

Verify the exact local snapshot and build the ignored canonical catalog:

```bash
uv run safecart-verify-manifest \
  data/manifests/bpom-cosmetics-2026-08-17.json "../dataset/Data BPOM"
uv run safecart-build-catalog "../dataset/Data BPOM" \
  data/processed/bpom-cosmetics.csv \
  --manifest data/manifests/bpom-cosmetics-2026-08-17.json
uv run safecart-generate-pairs data/processed/bpom-cosmetics.csv \
  data/processed/product-pairs.csv --seed 42
```

## Quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest --cov=safecart --cov-report=term-missing
```

## Repository boundaries

- Source datasets, generated pairs, model weights, and experiment outputs are ignored.
- Only small synthetic fixtures may be committed under `tests/fixtures/`.
- The mobile client lives in the separate `SafeCart-PWA` service repository and starts
  integration only after the AI acceptance gates in `docs/EXPERIMENT_PLAN.md` pass.
- Acquisition code lives in `SafeCart-ScrapingData` and is never a runtime dependency.
- Training code remains here because it produces the exact model served by this API;
  Kaggle is a compute environment, not a second source of truth.

Read `CONTRIBUTING.md` before creating a branch or commit.
