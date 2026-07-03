# AGENTS.md

Guidance for Codex or other coding agents working on this repository.

## Project purpose

This repository counts small two-terminal RLC one-port network topology classes.  The reference case is `R <= 3` and `L + C <= 5`, with L and C distinct, unordered terminals, unlabelled internal nodes, parallel branches allowed, no self-loops, and every support edge required to lie on a simple terminal-to-terminal path.

The current reference result is:

- `mode=lc`: total `1,408,796`; exactly `R=3` total `1,268,282`.
- `mode=generic`: total `57,945`; exactly `R=3` total `51,736`.

## Development environment

Use Python 3.11 or newer.

Recommended local setup:

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\Activate.ps1    # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

Do not commit `.venv/`, `__pycache__/`, build artefacts, or generated archives.

## Codex cloud expectations

A Codex cloud environment should need only:

1. a Python 3.11+ runtime;
2. network access for `pip install -e ".[dev]"` unless dependencies are pre-cached;
3. enough CPU for NetworkX isomorphism checks on graphs with at most eight support edges.

No external graph-generation binaries such as nauty/Traces are required.  The implementation uses NetworkX only.

## Validation commands

Run before committing changes:

```bash
pytest
python -m rlc_oneport_count --mode lc --max-r 3 --max-reactive 5
python -m rlc_oneport_count --mode generic --max-r 3 --max-reactive 5
```

The tests assert the reference tables.  If a change intentionally changes the counting assumptions, update `README.md`, `docs/computation.md`, `docs/results.md`, and the tests together.

## Important implementation details

- The terminal pair is unordered; terminal interchange is an allowed automorphism.
- Terminal-pair validity is based on simple path edge coverage, not merely on connectivity after edge deletion.
- Burnside's lemma is used for edge-bundle assignments.  Avoid replacing it with brute-force assignment enumeration unless the component budgets remain very small.
- `mode=lc` counts L and C as distinct branch types, but reports columns by `X = L + C`.
- `mode=generic` treats all reactive elements as a single type `X`.
