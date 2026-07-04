# 03-counting / 03 — Set enumeration scope: `R <= 3`, `L+C <= 5`

Status: `todo`

## Goal

Set the main enumeration target correctly.

## Correct scope

The planned counting scope is:

```text
R <= 3
L + C <= 5
```

That means up to three resistors and up to five reactive elements in total, where each reactive element is either an inductor or a capacitor.

This is not a request to count separate 3-element and 5-element networks. The `3` and `5` are independent upper bounds on element classes.

## Count grid

The full planned grid is:

```text
R count:      0, 1, 2, 3
L+C count:    0, 1, 2, 3, 4, 5
```

Before including degenerate cases in final tables, decide whether entries with no resistors, no reactive elements, or very small total element counts are useful or should be reported separately.

## Reactive assignments

For each reactive count `N = L+C`, counts may need to be split by `(L, C)` composition:

```text
N = 0: (L=0, C=0)
N = 1: (1,0), (0,1)
N = 2: (2,0), (1,1), (0,2)
...
N = 5: (5,0), (4,1), (3,2), (2,3), (1,4), (0,5)
```

## Done means

- The code accepts the scope as independent bounds on `R` and `L+C`.
- Count tables clearly label rows/columns as `R` and `L+C`.
- Tests cover boundary values, especially `R=3` and `L+C=5`.
