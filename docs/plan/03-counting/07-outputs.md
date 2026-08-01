# 03-counting / 07 — Store count outputs and supporting artefacts

Status: `prog`

## Goal

Make generated counts auditable without turning the repository into a dumping ground.

## Proposed locations

```text
data/counts/
  README.md
  small-r2-x3.json
  ladenheim.json
  full-r3-n5.json

docs/counts/
  small-r2-x3.md
  ladenheim.md
  full-r3-n5.md
```

Use the repository-wide `docs/` directory and the established slice spelling `r2-x3`, where `x` means `L+C`.

## Requirements

- Machine-readable data should be deterministic.
- Human-readable summaries should explain the definition used.
- Large generated artefacts should be reviewed before committing.

## Done means

- Count outputs can be regenerated.
- Diffs are meaningful.
- Documentation and data identify the same scope and definition.

## Progress notes

- Added the reviewable machine-readable summary `data/counts/small-r2-x3.json`
  and human summary `docs/counts/small-r2-x3.md`.
- Added the deterministic 148-record structural catalogue
  `data/counts/ladenheim-148.json`, its human contract summary
  `docs/counts/ladenheim-148.md`, and a check/write regeneration script. The
  full main-scope output and later Ladenheim outputs remain unfinished, so this
  task remains `prog`.
