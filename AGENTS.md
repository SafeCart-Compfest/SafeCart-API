# SafeCart API service agent rules

- Keep this repository limited to the public HTTP boundary and synchronous service
  orchestration.
- Do not add model training, OCR, retrieval, data acquisition, frontend code, or root
  deployment composition here.
- Explain affected files and the current flow before broad edits.
- Keep outbound integrations behind typed gateway interfaces.
- Preserve public response compatibility once `/v1/assessments` is released.
- Never output `FAKE`, `ILLEGAL`, or a legal/safety conclusion from listing evidence.
- Never store uploaded screenshots; process them in memory and enforce input limits.
- Do not commit datasets, model weights, secrets, generated artifacts, or institution
  branding.
- Use English for code, comments, identifiers, and commit messages.
- Run format, lint, type-check, tests, and Docker build when practical.
- Never commit, push, pull, merge, rebase, or create branches unless the user explicitly
  requests that Git action.
