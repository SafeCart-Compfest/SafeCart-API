# SafeCart monorepo agent rules

- Work AI-first. Do not add PWA integration until the experiment acceptance gates pass.
- Explain affected files and the current flow before broad edits.
- Keep public API, data schema, authentication, deployment, and CI changes explicit and
  separately approved.
- Keep the domain layer independent from FastAPI, OCR, storage, and model libraries.
- Treat all external records as versioned evidence, not unquestionable ground truth.
- Preserve multiple official candidates for the same NIE and abstain on ambiguity.
- Never output `FAKE`, `ILLEGAL`, or a legal/safety conclusion from listing evidence.
- Do not commit datasets, weights, secrets, generated artifacts, or institution branding.
- Use English for code, comments, identifiers, and commit messages.
- Run format, lint, type-check, and tests when practical.
- Never commit, push, pull, merge, rebase, or create branches unless the user explicitly
  requests that Git action.
