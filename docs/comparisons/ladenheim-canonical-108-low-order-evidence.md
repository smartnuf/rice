# Evidence for the low-order canonical Ladenheim networks

## 1. Purpose and production boundary

This report transcribes and independently matches the complete one-, two-, and
three-element portion of the canonical 108-network catalogue in A. Morelli and
M. C. Smith, *Passive Network Synthesis: An Approach to Classification*
(SIAM, 2019). It was prepared as a positive-identification evidence pilot,
separately from the later production application.

At this report's accepted evidence-only revision, production remained 40
excluded, 108 unresolved, and 0 retained.
At that milestone, every `basic_graph_assignment` was null and every
historical-identifier list was empty. The structural matches below did not
mark the 25 subjects retained, establish the complementary 108 as the
canonical catalogue, or begin the 108-to-62 classification.

The subsequent format-version-5 application retained and numbered all 25
reviewed subjects. At that application milestone, production became 40
excluded, 83 unresolved, and 25 retained.

The later complete four-element application retained and numbered another 34
reviewed subjects. At that milestone production became 40 excluded, 49
unresolved, and 59 retained. The subsequent complete five-element application
retains and numbers the remaining 49 canonical subjects. Current production is
40 excluded, 0 unresolved, and 108 retained, with 108 unique canonical
identifiers and all 148 `basic_graph_assignment` values still null. None of
these identity applications begins the 108-to-62 classification.

## 2. Source identity and exact locators

The inspected PDF was the existing read-only copy at
`../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf`.
Its SHA-256 is
`29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8`.
It was not copied into RICE.

| Material | Printed page | Zero-based PDF index | Evidence used |
|---|---:|---:|---|
| Table 6.2 | 49 | 55 | network, orbit, and equivalence-class counts by subfamily |
| Figure 6.1 | 50 | 56 | canonical numbers, the sole orbit in each subfamily, equivalence-class shading and labels, `p`/`s` orbit arrows, and dashed Zobel links |
| Table 6.11, low-order rows | 58 | 64 | equivalence-class labels and member network numbers |
| Appendix D, subfamilies IA, IB, and IIA | 135 | 141 | rendered primitive circuit diagrams |
| Appendix D, subfamilies IIB, IIIA, and IIIB | 136 | 142 | rendered primitive circuit diagrams |
| Appendix D, subfamilies IIIC, IIID, and IIIE | 137 | 143 | rendered primitive circuit diagrams |

All circuit topologies were transcribed from rendered Appendix D pages. Figure
6.1 was also rendered before reading its class shading, dashed equivalence
links, and transformation arrows. Extracted text was used only to locate and
cross-check labels and counts.

## 3. Authoritative inventory and terminology

Table 6.2 gives the following complete low-order inventory. Every subfamily is
one orbit under the source's `p` and `s` actions. Because the source does not
give a separate name to that sole orbit, this report records it as, for example,
“IIIA (sole orbit)”; this is a source-count statement, not a new orbit label.

| Element order | Subfamily | Networks | Orbits | Equivalence classes |
|---|---|---:|---:|---:|
| one | IA | 1 | 1 | 1 |
| one | IB | 2 | 1 | 2 |
| two | IIA | 4 | 1 | 4 |
| two | IIB | 2 | 1 | 2 |
| three | IIIA | 4 | 1 | 2 |
| three | IIIB | 4 | 1 | 2 |
| three | IIIC | 4 | 1 | 4 |
| three | IIID | 2 | 1 | 2 |
| three | IIIE | 2 | 1 | 2 |
| **Total** | **nine subfamilies** | **25** | **9** | **21** |

Figure 6.1 says that its dashed arrows are Zobel transformations and shades
multi-network equivalence classes. Thus networks 15 and 16 form class
`III_A^1`, networks 17 and 18 form `III_A^2`, networks 11 and 12 form
`III_B^1`, and networks 14 and 13 form `III_B^2`. Every other low-order class
has one network. The solid `p` and `s` arrows describe orbit membership; they do
not by themselves assert realizability-set equivalence.

## 4. Source transcription and RICE matches

Topology notation uses `--` for series and `||` for parallel composition.
Parentheses fix the independently transcribed grouping. `R2`, for example,
means two resistor primitives, not a component value or historical identity.
The class labels are normalized textual renderings of the source's superscript
notation.

| Canonical network | Elements | Inventory | Subfamily | Source equivalence class | Source orbit | Explicit coloured topology | Appendix D locator | Unique RICE catalogue ID | Representative descriptor |
|---:|---:|---|---|---|---|---|---|---|---|
| 3 | 1 | R1 | IA | `I_A^1` | IA (sole orbit) | `R` | p. 135 / index 141 | `lh148-e6719ebfaa65ecc4` | `0-1:R` |
| 1 | 1 | L1 | IB | `I_B^1` | IB (sole orbit) | `L` | p. 135 / index 141 | `lh148-11e22e7cba30a62f` | `0-1:L` |
| 2 | 1 | C1 | IB | `I_B^2` | IB (sole orbit) | `C` | p. 135 / index 141 | `lh148-187ef8e981d523c3` | `0-1:C` |
| 6 | 2 | R1 L1 | IIA | `II_A^1` | IIA (sole orbit) | `R -- L` | p. 135 / index 141 | `lh148-dacf11ef419be4ae` | `0-2:L;1-2:R` |
| 8 | 2 | R1 L1 | IIA | `II_A^2` | IIA (sole orbit) | `R || L` | p. 135 / index 141 | `lh148-33615cdca4d212bc` | `0-1:L;0-1:R` |
| 5 | 2 | R1 C1 | IIA | `II_A^3` | IIA (sole orbit) | `R -- C` | p. 135 / index 141 | `lh148-e5ab4cbd88b9cfcd` | `0-2:C;1-2:R` |
| 9 | 2 | R1 C1 | IIA | `II_A^4` | IIA (sole orbit) | `R || C` | p. 135 / index 141 | `lh148-e798eb374bc4314b` | `0-1:C;0-1:R` |
| 4 | 2 | L1 C1 | IIB | `II_B^1` | IIB (sole orbit) | `L -- C` | p. 136 / index 142 | `lh148-bc703386759e1fc4` | `0-2:C;1-2:L` |
| 7 | 2 | L1 C1 | IIB | `II_B^2` | IIB (sole orbit) | `L || C` | p. 136 / index 142 | `lh148-6c4acdd4ee210778` | `0-1:C;0-1:L` |
| 15 | 3 | R2 L1 | IIIA | `III_A^1` | IIIA (sole orbit) | `R -- (R || L)` | p. 136 / index 142 | `lh148-d0dd7ab06f8d9467` | `0-2:L;0-2:R;1-2:R` |
| 16 | 3 | R2 L1 | IIIA | `III_A^1` | IIIA (sole orbit) | `R || (R -- L)` | p. 136 / index 142 | `lh148-26ab596fc1b6adf0` | `0-1:R;0-2:L;1-2:R` |
| 17 | 3 | R2 C1 | IIIA | `III_A^2` | IIIA (sole orbit) | `R -- (R || C)` | p. 136 / index 142 | `lh148-f2ca341555f420ec` | `0-2:C;0-2:R;1-2:R` |
| 18 | 3 | R2 C1 | IIIA | `III_A^2` | IIIA (sole orbit) | `R || (R -- C)` | p. 136 / index 142 | `lh148-2d28eb19a83067c3` | `0-1:R;0-2:C;1-2:R` |
| 11 | 3 | R1 L2 | IIIB | `III_B^1` | IIIB (sole orbit) | `L -- (R || L)` | p. 136 / index 142 | `lh148-9ce47e2e00e47d8a` | `0-2:L;0-2:R;1-2:L` |
| 12 | 3 | R1 L2 | IIIB | `III_B^1` | IIIB (sole orbit) | `L || (R -- L)` | p. 136 / index 142 | `lh148-ba7c48b07f29dd51` | `0-1:L;0-2:L;1-2:R` |
| 14 | 3 | R1 C2 | IIIB | `III_B^2` | IIIB (sole orbit) | `C -- (R || C)` | p. 136 / index 142 | `lh148-34b077a26df0d439` | `0-2:C;0-2:R;1-2:C` |
| 13 | 3 | R1 C2 | IIIB | `III_B^2` | IIIB (sole orbit) | `C || (R -- C)` | p. 136 / index 142 | `lh148-4ec3374bd9f5ab9d` | `0-1:C;0-2:C;1-2:R` |
| 41 | 3 | R1 L1 C1 | IIIC | `III_C^1` | IIIC (sole orbit) | `L || (R -- C)` | p. 137 / index 143 | `lh148-6ab986b43f5cdc3d` | `0-1:L;0-2:C;1-2:R` |
| 34 | 3 | R1 L1 C1 | IIIC | `III_C^2` | IIIC (sole orbit) | `L -- (R || C)` | p. 137 / index 143 | `lh148-81fbe344564bbcf0` | `0-2:C;0-2:R;1-2:L` |
| 49 | 3 | R1 L1 C1 | IIIC | `III_C^3` | IIIC (sole orbit) | `(R -- L) || C` | p. 137 / index 143 | `lh148-7ad37b581984a1b6` | `0-1:C;0-2:L;1-2:R` |
| 26 | 3 | R1 L1 C1 | IIIC | `III_C^4` | IIIC (sole orbit) | `C -- (R || L)` | p. 137 / index 143 | `lh148-aecc406cd94c57bc` | `0-2:C;1-2:L;1-2:R` |
| 27 | 3 | R1 L1 C1 | IIID | `III_D^1` | IIID (sole orbit) | `R -- (L || C)` | p. 137 / index 143 | `lh148-c4dd949e0cc0cb9a` | `0-2:C;0-2:L;1-2:R` |
| 42 | 3 | R1 L1 C1 | IIID | `III_D^2` | IIID (sole orbit) | `R || (C -- L)` | p. 137 / index 143 | `lh148-0fa59ac63267cb6f` | `0-1:R;0-2:C;1-2:L` |
| 10 | 3 | R1 L1 C1 | IIIE | `III_E^1` | IIIE (sole orbit) | `R -- L -- C` | p. 137 / index 143 | `lh148-ec2d91a9eb609e87` | `0-2:C;1-3:L;2-3:R` |
| 19 | 3 | R1 L1 C1 | IIIE | `III_E^2` | IIIE (sole orbit) | `R || L || C` | p. 137 / index 143 | `lh148-f6b0120a6632013a` | `0-1:C;0-1:L;0-1:R` |

Figure 6.1 (printed page 50 / index 56) and Table 6.11 (printed page
58 / index 64) are the locators for every class and orbit entry in this table;
the Appendix D column locates the independently rendered topology.

## 5. Structural matching method and result

Each table topology was separately encoded as a `PrimitiveNetwork` with an
unordered terminal pair and primitive coloured `PrimitiveEdge` objects. The
complete 148-record catalogue was independently indexed with
`network_from_descriptor` and `canonical_structural_signature`. Matching used
exactly the committed
`colour-preserving-port-augmented-cycle-matroid-v1` relation. Descriptor text,
catalogue ordering, source ordering, duality, frequency inversion, and
subfamily counts were not matching predicates.

Every fixture has exactly one signature match. The 25 matches use 25 different
RICE catalogue IDs, have the source-drawn component inventories, and were all
`unresolved` in the production ledger at the accepted evidence-only revision.
None was among the forty excluded rows. The result therefore establishes
subject identity under the
committed structural relation, but this evidence-only report does not apply a
canonical number or positive disposition.

## 6. Equivalence and orbit boundary

Morelli and Smith state the equivalence-class and orbit structure shown in
Figure 6.1 and tabulated in Tables 6.2 and 6.11. The RICE computation in this
report checks only coloured two-terminal structural identity between each
rendered source fixture and a catalogue subject. It does not reproduce the
source's realizability-set equivalence relation.

In particular, the sole-orbit subfamily membership does not prove equivalence;
the `p` and `s` group actions are not equivalence-class membership; and the
dashed Zobel arrows are recorded source relationships rather than a general
RICE equivalence contract. The 21 source equivalence classes are evidence for a
later classification milestone, not a claim that RICE has reproduced all 62.

## 7. Previous-workspace audit

This audit was performed only after the PDF transcription and RICE matching
were complete. The sibling repositories were read-only and clean at:

- `../network-theory` commit
  `87b831831c154c5c3675853a99ff7e5a2b7dfb6d`;
- `../pynntt` commit `f3db06032cbe23d583d77f6cb79d21ced90d7651`;
- `../pynntt_lab` commit `1ddd90034da4594bb6a3728b0700918883fd1172`.

The `network-theory` directory
`016--graph-generation/doc/ladenheim-catalogue/ladenheim-schematics/`
contains nonempty numbered PNGs for all 25 source numbers. A bounded visual
sample (networks 1, 6, 15, 16, 19, and 41) agrees with the independent Appendix
D transcription. The files use heterogeneous dimensions and colour modes, so
they are not treated as a normalized machine fixture set. No relevant
low-order numbering or RICE-ID mapping was found in the bounded `pynntt` or
`pynntt_lab` search. No sibling file supplied a topology, class allocation,
canonical number, or RICE ID used above.

## 8. Conclusions and limitations

The authoritative low-order inventory is 3 one-element, 6 two-element, and 16
three-element networks: 25 networks in nine subfamilies, nine orbits, and 21
equivalence classes. Independently transcribed coloured fixtures select exactly
25 distinct RICE subjects, one per canonical source diagram; all 25 were
unresolved at the accepted evidence-only revision.

This evidence supported the later subject-bound canonical-identity application.
That application now retains and numbers the complete reviewed 25-member group
without changing the durable structural result reported here. It does not make
a complete canonical-108 reproduction claim or begin the 108-to-62 behavioural
classification.

The subsequent four-element application raises the positively identified total
to 59 without changing the durable low-order structural matches reported here.
The later five-element application completes the 108 identified canonical
subjects without changing those durable low-order matches.

## 9. Reproduction commands

The exact block below records the evidence-only state at accepted commit
`4411b1fa441241f47e3d2e39a4e96ef5447199e9`. Its unresolved-row and
40 excluded / 108 unresolved / 0 retained assertions are historical acceptance
checks. The reusable computation result is the unique structural
correspondence, descriptors, and component inventories. After a later identity
application, reproducing this historical block requires checking out the pinned
commit. After the low-order application, production was 40 excluded, 83
unresolved, and 25 retained; after the four-element application it was 40
excluded, 49 unresolved, and 59 retained. Current production after the complete
five-element application is 40 excluded, 0 unresolved, and 108 retained. The
current state is validated separately by the current canonical-identity
contract, generator, and tests.

Run this paste-ready block from the RICE repository root. It uses only existing
RICE APIs and the Python standard library, scans all 148 catalogue rows, and
fails on a missing, duplicate, excluded, or non-unique match.

```bash
.venv/bin/python - <<'PY'
import json
from collections import Counter
from pathlib import Path

from rice.ladenheim import (
    PrimitiveEdge,
    PrimitiveNetwork,
    canonical_structural_signature,
    network_from_descriptor,
)


RELATION = "colour-preserving-port-augmented-cycle-matroid-v1"


def network(edges):
    return PrimitiveNetwork(
        ("A", "Z"),
        tuple(PrimitiveEdge(u, v, colour) for u, v, colour in edges),
    )


def series(*colours):
    nodes = ["A"] + [f"n{i}" for i in range(1, len(colours))] + ["Z"]
    return network([
        (nodes[i], nodes[i + 1], colour)
        for i, colour in enumerate(colours)
    ])


def parallel(*arms):
    edges = []
    for arm_index, colours in enumerate(arms):
        nodes = ["A"] + [
            f"a{arm_index}n{i}" for i in range(1, len(colours))
        ] + ["Z"]
        edges.extend(
            (nodes[i], nodes[i + 1], colour)
            for i, colour in enumerate(colours)
        )
    return network(edges)


def leading_then_parallel(leading, first, second):
    return network([
        ("A", "B", leading),
        ("B", "Z", first),
        ("B", "Z", second),
    ])


fixtures = {
    1: series("L"),
    2: series("C"),
    3: series("R"),
    4: series("L", "C"),
    5: series("R", "C"),
    6: series("R", "L"),
    7: parallel(("L",), ("C",)),
    8: parallel(("R",), ("L",)),
    9: parallel(("R",), ("C",)),
    10: series("R", "L", "C"),
    11: leading_then_parallel("L", "R", "L"),
    12: parallel(("L",), ("R", "L")),
    13: parallel(("C",), ("R", "C")),
    14: leading_then_parallel("C", "R", "C"),
    15: leading_then_parallel("R", "R", "L"),
    16: parallel(("R",), ("R", "L")),
    17: leading_then_parallel("R", "R", "C"),
    18: parallel(("R",), ("R", "C")),
    19: parallel(("R",), ("L",), ("C",)),
    26: leading_then_parallel("C", "R", "L"),
    27: leading_then_parallel("R", "L", "C"),
    34: leading_then_parallel("L", "R", "C"),
    41: parallel(("L",), ("R", "C")),
    42: parallel(("R",), ("C", "L")),
    49: parallel(("R", "L"), ("C",)),
}

metadata = {
    1: ("IB", "I_B^1", (0, 1, 0)),
    2: ("IB", "I_B^2", (0, 0, 1)),
    3: ("IA", "I_A^1", (1, 0, 0)),
    4: ("IIB", "II_B^1", (0, 1, 1)),
    5: ("IIA", "II_A^3", (1, 0, 1)),
    6: ("IIA", "II_A^1", (1, 1, 0)),
    7: ("IIB", "II_B^2", (0, 1, 1)),
    8: ("IIA", "II_A^2", (1, 1, 0)),
    9: ("IIA", "II_A^4", (1, 0, 1)),
    10: ("IIIE", "III_E^1", (1, 1, 1)),
    11: ("IIIB", "III_B^1", (1, 2, 0)),
    12: ("IIIB", "III_B^1", (1, 2, 0)),
    13: ("IIIB", "III_B^2", (1, 0, 2)),
    14: ("IIIB", "III_B^2", (1, 0, 2)),
    15: ("IIIA", "III_A^1", (2, 1, 0)),
    16: ("IIIA", "III_A^1", (2, 1, 0)),
    17: ("IIIA", "III_A^2", (2, 0, 1)),
    18: ("IIIA", "III_A^2", (2, 0, 1)),
    19: ("IIIE", "III_E^2", (1, 1, 1)),
    26: ("IIIC", "III_C^4", (1, 1, 1)),
    27: ("IIID", "III_D^1", (1, 1, 1)),
    34: ("IIIC", "III_C^2", (1, 1, 1)),
    41: ("IIIC", "III_C^1", (1, 1, 1)),
    42: ("IIID", "III_D^2", (1, 1, 1)),
    49: ("IIIC", "III_C^3", (1, 1, 1)),
}

expected_subfamilies = {
    "IA": (1, 1),
    "IB": (2, 2),
    "IIA": (4, 4),
    "IIB": (2, 2),
    "IIIA": (4, 2),
    "IIIB": (4, 2),
    "IIIC": (4, 4),
    "IIID": (2, 2),
    "IIIE": (2, 2),
}

catalogue = json.loads(Path("data/counts/ladenheim-148.json").read_text())
ledger = json.loads(
    Path("data/comparisons/ladenheim-148-to-108.json").read_text()
)
assert len(catalogue["records"]) == 148
assert ledger["summary"]["by_proposed_disposition"] == {
    "exclude": 40,
    "unresolved": 108,
}
assert all(row["basic_graph_assignment"] is None for row in ledger["records"])
assert all(row["historical_identifiers"] == [] for row in ledger["records"])

ledger_rows = {row["catalogue_id"]: row for row in ledger["records"]}
catalogue_by_signature = {}
for row in catalogue["records"]:
    signature = canonical_structural_signature(
        network_from_descriptor(row["representative_descriptor"])
    )
    assert signature.relation == RELATION
    catalogue_by_signature.setdefault(signature, []).append(row)

matches = {}
for number in sorted(fixtures):
    signature = canonical_structural_signature(fixtures[number])
    assert signature.relation == RELATION
    rows = catalogue_by_signature.get(signature, [])
    assert len(rows) == 1, (number, [row["catalogue_id"] for row in rows])
    row = rows[0]
    subfamily, eq_class, inventory = metadata[number]
    assert (row["r"], row["l"], row["c"]) == inventory
    production_row = ledger_rows[row["catalogue_id"]]
    assert production_row["comparison_status"] == "unresolved"
    assert production_row["proposed_disposition"] == "unresolved"
    assert production_row["exclusion_category"] == "unresolved"
    matches[number] = row
    print(
        f"network {number:>2} {subfamily} {eq_class} -> "
        f"{row['catalogue_id']} {row['representative_descriptor']}"
    )

assert len(fixtures) == 25
assert len(matches) == 25
assert len({row["catalogue_id"] for row in matches.values()}) == 25
assert Counter(sum(metadata[number][2]) for number in metadata) == {
    1: 3,
    2: 6,
    3: 16,
}
for subfamily, (network_count, class_count) in expected_subfamilies.items():
    numbers = [
        number for number, value in metadata.items() if value[0] == subfamily
    ]
    assert len(numbers) == network_count
    assert len({metadata[number][1] for number in numbers}) == class_count
assert sum(value[0] for value in expected_subfamilies.values()) == 25
assert sum(value[1] for value in expected_subfamilies.values()) == 21
assert len(expected_subfamilies) == 9

print("counts by element order: 1=3, 2=6, 3=16; total=25")
print("source structure: 9 subfamilies, 9 orbits, 21 equivalence classes")
print("structural matches: 25 unique unresolved RICE subjects; no duplicates")
print("historical evidence-only baseline: 40 excluded / 108 unresolved / 0 retained")
PY
```

The observed output is recorded after executing this exact block in the
validation section below.

## 10. Observed reproduction output

```text
network  1 IB I_B^1 -> lh148-11e22e7cba30a62f 0-1:L
network  2 IB I_B^2 -> lh148-187ef8e981d523c3 0-1:C
network  3 IA I_A^1 -> lh148-e6719ebfaa65ecc4 0-1:R
network  4 IIB II_B^1 -> lh148-bc703386759e1fc4 0-2:C;1-2:L
network  5 IIA II_A^3 -> lh148-e5ab4cbd88b9cfcd 0-2:C;1-2:R
network  6 IIA II_A^1 -> lh148-dacf11ef419be4ae 0-2:L;1-2:R
network  7 IIB II_B^2 -> lh148-6c4acdd4ee210778 0-1:C;0-1:L
network  8 IIA II_A^2 -> lh148-33615cdca4d212bc 0-1:L;0-1:R
network  9 IIA II_A^4 -> lh148-e798eb374bc4314b 0-1:C;0-1:R
network 10 IIIE III_E^1 -> lh148-ec2d91a9eb609e87 0-2:C;1-3:L;2-3:R
network 11 IIIB III_B^1 -> lh148-9ce47e2e00e47d8a 0-2:L;0-2:R;1-2:L
network 12 IIIB III_B^1 -> lh148-ba7c48b07f29dd51 0-1:L;0-2:L;1-2:R
network 13 IIIB III_B^2 -> lh148-4ec3374bd9f5ab9d 0-1:C;0-2:C;1-2:R
network 14 IIIB III_B^2 -> lh148-34b077a26df0d439 0-2:C;0-2:R;1-2:C
network 15 IIIA III_A^1 -> lh148-d0dd7ab06f8d9467 0-2:L;0-2:R;1-2:R
network 16 IIIA III_A^1 -> lh148-26ab596fc1b6adf0 0-1:R;0-2:L;1-2:R
network 17 IIIA III_A^2 -> lh148-f2ca341555f420ec 0-2:C;0-2:R;1-2:R
network 18 IIIA III_A^2 -> lh148-2d28eb19a83067c3 0-1:R;0-2:C;1-2:R
network 19 IIIE III_E^2 -> lh148-f6b0120a6632013a 0-1:C;0-1:L;0-1:R
network 26 IIIC III_C^4 -> lh148-aecc406cd94c57bc 0-2:C;1-2:L;1-2:R
network 27 IIID III_D^1 -> lh148-c4dd949e0cc0cb9a 0-2:C;0-2:L;1-2:R
network 34 IIIC III_C^2 -> lh148-81fbe344564bbcf0 0-2:C;0-2:R;1-2:L
network 41 IIIC III_C^1 -> lh148-6ab986b43f5cdc3d 0-1:L;0-2:C;1-2:R
network 42 IIID III_D^2 -> lh148-0fa59ac63267cb6f 0-1:R;0-2:C;1-2:L
network 49 IIIC III_C^3 -> lh148-7ad37b581984a1b6 0-1:C;0-2:L;1-2:R
counts by element order: 1=3, 2=6, 3=16; total=25
source structure: 9 subfamilies, 9 orbits, 21 equivalence classes
structural matches: 25 unique unresolved RICE subjects; no duplicates
historical evidence-only baseline: 40 excluded / 108 unresolved / 0 retained
```
