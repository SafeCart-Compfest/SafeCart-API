# Contributing

## Development principles

- Prefer small, testable changes that preserve the API contract.
- Keep public schemas and orchestration independent from HTTP client implementations.
- Do not commit secrets, personal data, uploaded screenshots, or generated artifacts.
- Do not claim that a result proves a product is authentic, safe, or illegal.
- Do not show educational institution names or branding in competition artifacts.

## Branch workflow

`main` is the protected, reproducible branch. Do not push directly to it.

1. Update local `main` with `git pull --ff-only`.
2. Create a short-lived branch: `feat/...`, `fix/...`, `experiment/...`, `docs/...`, or
   `chore/...`.
3. Commit each coherent change with tests and a descriptive Conventional Commit.
4. Push the branch and open a pull request.
5. Complete the self-review checklist and require every configured quality check to pass.
6. Delete the merged branch. Never force-push a shared branch.

Examples:

```text
feat(api): accept validated assessment uploads
fix(readiness): map AI timeouts to service unavailable
refactor(client): isolate AI transport adapter
docs(api): document assessment error responses
```

## Pull request checklist

- Scope and motivation are explicit.
- Public contract and downstream compatibility impacts are documented.
- Input limits and failure mappings are explicit.
- Tests cover the changed behavior.
- README or API documentation is updated when setup or behavior changes.
- No institution branding, credentials, large data, or generated files are included.

## Recommended GitHub settings

Configure these in the organization after the team agrees:

- Protect `main`; require pull requests and resolved conversations. Approval count is zero
  for the preliminary sprint, so the author must perform the documented self-review.
- Require the test, lint, and type-check jobs before merge.
- Block force pushes and branch deletion on `main`.
- Enable secret scanning and dependency alerts.
- Keep an immutable tag for the preliminary submission commit.

Repository settings are not changed by this document.
