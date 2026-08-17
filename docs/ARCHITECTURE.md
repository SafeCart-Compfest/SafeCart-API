# Architecture

## Decision

SafeCart is a listing identity consistency and compliance-triage system. The core
research question is whether a fine-tuned pair matcher detects subtle listing-to-record
mismatches that exact NIE lookup and lexical similarity miss.

## Target components

1. OCR adapter extracts text, bounding boxes, and confidence from one listing screenshot.
2. Entity extraction normalizes NIE, brand, product name, variant, and package.
3. Retrieval returns all exact NIE matches or top-k semantic candidates.
4. A fine-tuned matcher classifies `MATCH`, `MISMATCH`, or `INSUFFICIENT_EVIDENCE`.
5. Calibration and deterministic field evidence produce a review status.
6. FastAPI exposes one synchronous assessment operation to the PWA.

## Dependency direction

```text
HTTP/OCR/storage adapters -> application orchestration -> domain models and policies
```

The domain layer must not import FastAPI, OCR libraries, databases, or model frameworks.
Model and baseline implementations share an application-level matcher interface when
the trained model is added.

## Critical invariant

An NIE is not assumed to identify exactly one row. Snapshots and the public portal can
contain multiple distinct records for the same NIE. Retrieval must preserve all records,
attach source and snapshot metadata, and route ambiguity to human review.

## API scope for the preliminary round

- One synchronous assessment input and one evidence-report output.
- No authentication, background jobs, crawler, distributed database, or automatic
  takedown.
- The current `/_internal/baseline/assessments` route accepts structured candidates for
  baseline testing only. The public assessment contract will be designed after OCR and
  the trained matcher meet their acceptance gates; clients must never supply or spoof
  official evidence.
