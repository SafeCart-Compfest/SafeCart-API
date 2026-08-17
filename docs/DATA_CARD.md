# Data card

## Local inventory observed on 2026-08-17

### BPOM snapshot

- Five CSV files, 661,894 rows, 18 columns.
- 364,133 rows are labeled `Kosmetik`.
- 275,415 unique cosmetic NIE strings.
- 88,523 repeated cosmetic business records after ignoring source row IDs.
- 192 NIE values map to more than one distinct identity tuple in the snapshot.
- At least one ambiguity (`NA18241700093`) was also visible in the public Cek BPOM
  portal during the audit.

The files are useful for retrieval, hard-negative discovery, and schema exploration.
They are not automatically accepted as clean labels. Record-level provenance, snapshot
date, extraction method, permission/license, and reconciliation policy are still needed.

### Roboflow counterfeit medicine detection

- 4,259 images in the local split (4,072 train, 122 validation, 65 test).
- 7,637 bounding boxes: 6,989 `authentic` and 648 `counterfeit`.
- CC BY 4.0 according to its included metadata.
- Images are resized to 640x640 and heavily augmented; only 253 unique source-name
  stems appear in the 4,072 training images.
- The subject is counterfeit medicine imagery, not Indonesian cosmetic listing identity.

Use only as an optional visual ablation. It cannot provide the ground truth for the core
SafeCart claim.

### Sociolla skincare collection

- 91 product rows with product metadata and BPOM IDs.
- 747 ingredient-category rows.
- Images are separated into `genuine_reference` and
  `reported_counterfeit_candidate` folders.
- Only 65 of 90 unique BPOM IDs in the product table were found in the local BPOM CSV
  snapshot during the 2026-08-17 audit. This 72.2% coverage is too low to treat the
  snapshot as a complete official catalog.

The word `reported` is essential: a reported candidate is not verified counterfeit
ground truth. Confirm source terms, consent, redistribution rights, and label procedure
before any training or public release.

The supplied Kaggle dataset URL returned a not-found page during the audit. Publication
visibility and a stable versioned download must be fixed before it can serve as
submission provenance.

### BPOM image collections

These are potentially useful for OCR stress tests and qualitative demonstrations. Folder
names alone are not sufficient labeling methodology. Preserve the original publication
URL, publication date, and meaning of each category.

## Required core dataset

Each example must contain:

```text
listing identity + official candidate(s) + pair label + reason codes + provenance
```

Required label states are `MATCH`, `MISMATCH`, and `INSUFFICIENT_EVIDENCE`. Mismatch
reasons include NIE, brand, product family, variant, package, and official-record
ambiguity.

## Split policy

- Split by product family or canonical SKU before generating mutations.
- Keep every augmentation and mutation of one source product in one split.
- Maintain a real, manually reviewed, unseen-listing test set.
- Synthetic hard negatives may train the model but may not be the only headline test.
- Report results separately for exact matches, hard negatives, OCR degradation,
  ambiguous official records, and unseen brands/products.
