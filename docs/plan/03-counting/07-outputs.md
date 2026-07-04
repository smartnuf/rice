# 03-counting / 07 — Store count outputs and supporting artefacts

Status: `todo`

## Goal

Make generated counts auditable without turning the repository into a dumping ground.

## Proposed locations

```text
data/counts/
  README.md
  small-r2-n3.json
  ladenheim.json
  full-r3-n5.json

doc/counts/
  small-r2-n3.md
  ladenheim.md
  full-r3-n5.md
```

Here `n` means `L+C`.

## Requirements

- Machine-readable data should be deterministic.
- Human-readable summaries should explain the definition used.
- Large generated artefacts should be reviewed before committing.

## Done means

- Count outputs can be regenerated.
- Diffs are meaningful.
- Documentation and data identify the same scope and definition.
