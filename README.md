# RLC one-port topology counter

This project counts small connected two-terminal RLC one-port network topology classes.  It was created to reproduce and extend the count for networks built using at most three resistors and at most five reactive elements.

The main case of interest is:

> **R <= 3, L + C <= 5, with inductors and capacitors counted as distinct branch types.**

Under the assumptions below, the count is:

- **1,408,796** networks with **at most 3 R** and **at most 5 L+C**;
- **1,268,282** networks with **exactly 3 R** and **at most 5 L+C**.

## Counting assumptions

A network is counted as a graph-theoretic one-port topology:

- the two terminal nodes form an unordered terminal pair, so swapping the terminals does not create a new network;
- internal nodes are unlabelled;
- branches are labelled by component type;
- in `lc` mode, branch types are `R`, `L`, and `C`;
- in `generic` mode, branch types are `R` and generic reactive `X`;
- parallel branches are allowed;
- self-loops are not allowed;
- every branch must lie on at least one **simple** path between the two terminals, so dangling appendages and branches that only occur in non-simple walks are excluded.

Equivalently, the code first counts simple two-terminal support graphs and then counts non-empty parallel bundles on each support edge.

## Results

### Distinct L and C reactive elements

The table entry is the number of networks having exactly `R` resistors and exactly `X = L + C` reactive elements, summed over all L/C splittings.

| R \ X=L+C | 0 | 1 | 2 | 3 | 4 | 5 | Row total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 2 | 6 | 22 | 106 | 596 | 732 |
| 1 | 1 | 4 | 24 | 160 | 1,205 | 9,668 | 11,062 |
| 2 | 2 | 14 | 128 | 1,186 | 11,582 | 115,808 | 128,720 |
| 3 | 4 | 48 | 634 | 7,878 | 96,376 | 1,163,342 | **1,268,282** |

Grand total for `R <= 3, L+C <= 5`: **1,408,796**.

### Generic reactive element X

This is the simpler count where all reactive elements are a single generic type `X`.

| R \ X | 0 | 1 | 2 | 3 | 4 | 5 | Row total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 2 | 4 | 11 | 31 | 49 |
| 1 | 1 | 2 | 7 | 24 | 97 | 403 | 534 |
| 2 | 2 | 7 | 36 | 170 | 875 | 4,536 | 5,626 |
| 3 | 4 | 24 | 170 | 1,083 | 6,928 | 43,527 | **51,736** |

Grand total for `R <= 3, X <= 5`: **57,945**.

### Support graph count

For the `R <= 3, reactive <= 5` run, the maximum number of support edges is eight.  The relevant simple two-terminal support graphs are counted as follows:

| Support edges | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 1 | 1 | 2 | 4 | 10 | 27 | 80 | 258 | **383** |

## Method

The computation is support-graph based.

1. Enumerate all connected unlabelled simple support graphs with up to `max_r + max_reactive` edges.
2. For each support graph, find unordered terminal-pair orbits under graph automorphisms.
3. Keep only terminal pairs for which every support edge lies on at least one simple terminal-to-terminal path.
4. For each terminal support graph, compute the automorphism group preserving the terminal set. Terminal interchange is allowed.
5. Count non-empty branch bundles on support edges using Burnside's lemma.  A bundle is either `(r, x)` in generic mode or `(r, l, c)` in L/C mode.
6. Sum orbit counts by total resistor count and total reactive count.

The important subtlety is step 3: an edge is not accepted merely because it appears in a terminal-to-terminal walk.  It must occur in at least one **simple** terminal-to-terminal path.

## Use

Create and activate a virtual environment locally:

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\Activate.ps1    # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the tests:

```bash
pytest
```

Run the main count:

```bash
rlc-oneport-count --mode lc --max-r 3 --max-reactive 5
```

Or without installing the console script:

```bash
python -m rlc_oneport_count --mode lc --max-r 3 --max-reactive 5
```

JSON output is also available:

```bash
rlc-oneport-count --mode lc --format json
```

## Repository note

Do not commit a real `.venv` directory.  It is platform-specific, can be large, and is already excluded by `.gitignore`.  Commit the source, tests, documentation, and `pyproject.toml`; recreate `.venv` in each development environment.
