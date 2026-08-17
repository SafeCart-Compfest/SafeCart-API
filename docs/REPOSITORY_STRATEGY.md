# Repository strategy

SafeCart uses five repositories with the `SafeCart-{Purpose}` convention:

- `SafeCart-PWA`: mobile-first frontend.
- `SafeCart-API`: public gateway and orchestration.
- `SafeCart-AI`: data preparation, training, evaluation, and private inference.
- `SafeCart-ScrapingData`: offline source acquisition; not a runtime dependency.
- `SafeCart-Deployment`: primary submission link, pinned versions, setup guide, and
  Docker Compose.

Only PWA, API, and AI are runtime services. A new repository requires an independent
ownership and release boundary; small modules remain in their owning service.

Competition repositories are public, while secrets, raw sources, private screenshots,
generated datasets, and model weights stay outside Git. Deployment consumes immutable,
checksummed AI artifacts and never scrapes during evaluation.
