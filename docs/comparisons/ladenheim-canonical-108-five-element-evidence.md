# Canonical 108 five-element evidence

## 1. Purpose and production boundary

This report independently transcribes and structurally matches the complete
five-element portion of the canonical 108-network Ladenheim catalogue. Morelli
and Smith are authoritative for the numbered diagrams, subfamilies, orbits,
equivalence classes, and network types. The `lh148-*` correspondences are
independently reproduced RICE structural facts; the publication does not print
RICE catalogue identifiers.

At this report's original evidence-only milestone, production remained 40 excluded,
49 unresolved, and 59 retained. The already applied 25 low-order and 34
four-element canonical identities were unchanged. The 49 matches below were
unresolved and carried no historical identifiers. All 148
`basic_graph_assignment` values remained null. No format-version-6 contract,
structured annotation evidence, production disposition, or 108-to-62
classification was changed at that milestone.

Subsequently, format version 6 encoded the complete controlled 49-member
five-element group: 49 authoritative definitions, 49 exact subject-bound RICE
matches, one aggregate, and one pinned computation. The later complete
application now retains and numbers all 49 subjects through that group. Current
production is 40 excluded, 0 unresolved, and 108 retained, with 108 unique
canonical identifiers and all 148 graph assignments null. The reproduction
block below remains a historical record pinned to accepted evidence revision
`b64946fd9ddcae6f764921d082b315affb9e233e`.

## 2. Source identity and exact locators

The authority is A. Morelli and M. C. Smith, *Passive Network Synthesis: An
Approach to Classification*, SIAM, 2019. The existing read-only PDF used by the
earlier Ladenheim investigations has SHA-256
`29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8`.
It was not copied into this repository.

| Material | Printed page | Zero-based PDF index | Use |
|---|---:|---:|---|
| Tables 6.2 and 6.3 | 49 | 55 | Aggregate counts and network-type allocation |
| Figure 6.3 | 51 | 57 | Solid `p`/`s` orbit edges, dashed equivalences, and class shading |
| Table 6.11, five-element rows | 59--61 | 65--67 | Exact source equivalence classes |
| Appendix D, subfamily VA | 141 | 147 | Numbered coloured diagrams |
| Appendix D, subfamilies VB, VC, VD | 142 | 148 | Numbered coloured diagrams |
| Appendix D, subfamily VE | 143 | 149 | Numbered coloured diagrams |
| Appendix D, subfamilies VF, VG, VH, VI | 144 | 150 | Numbered coloured diagrams |

Rendered pages, rather than parsed PDF text, were used for topology, terminal
placement, component kinds, node incidence, solid orbit edges, dashed links,
Y-delta labels, and class shading.

## 3. Source terminology and aggregate inventory

A canonical number identifies one particular coloured two-terminal diagram.
A subfamily is a source organizational category. A group-action orbit is the
set connected by the solid `p` and `s` actions in Figure 6.3. A realizability-
set equivalence class is the source class in Figure 6.3 and Table 6.11; it is
not an orbit and is not established by a structural graph match. Table 6.3's
network type is further source context, not a visual inference from how a
drawing is laid out.

| Subfamily | Networks | Equivalence classes | Orbits | Source network type |
|---|---:|---:|---:|---|
| VA | 12 | 2 | 3 | simple series-parallel |
| VB | 8 | 4 | 2 | series-parallel |
| VC | 2 | 2 | 1 | bridge |
| VD | 2 | 2 | 1 | bridge |
| VE | 12 | 4 | 3 | simple series-parallel |
| VF | 6 | 2 | 2 | series-parallel |
| VG | 4 | 2 | 2 | series-parallel / bridge |
| VH | 2 | 2 | 1 | bridge |
| VI | 1 | 1 | 1 | bridge |
| **Total** | **49** | **21** | **16** | -- |

The source diagrams give 12 networks with inventory R3/L2/C0, 12 with
R3/L0/C2, and 25 with R3/L1/C1. Every diagram therefore contains three
resistors and two reactive elements.

The solid-edge orbit sets transcribed from Figure 6.3 are:

- VA: `{52,56,77,81}`, `{50,54,75,79}`, `{51,55,76,80}`;
- VB: `{58,59,83,84}`, `{53,57,78,82}`;
- VC: `{60,85}`; VD: `{61,86}`;
- VE: `{66,69,90,94}`, `{65,68,91,93}`, `{64,67,89,92}`;
- VF: `{99,100,102,103}`, `{98,101}`;
- VG: `{104,106}`, `{105,107}`; VH: `{70,95}`; VI: `{108}`.

Figure 6.3 states that dashed equivalences are Zobel transformations unless
labelled otherwise. The vertical links 104--105 and 106--107 are explicitly
labelled Y-delta; the other dashed links are Zobel relationships. No Zobel,
Y-delta, `p`, or `s` transformation contract is implemented by this report.

## 4. Authoritative source transcription

In the topology column, `A` and `Z` are the unordered terminals and every
listed edge is primitive and coloured. Internal node names are local to a row.
`App`, `Fig`, and `Tbl` give printed-page/PDF-index locators. A multi-network
class has a Zobel link unless the row is one of the explicitly labelled VG
Y-delta endpoints.

| No. | R/L/C | Subf. | Source class | Exact source orbit | Type | Explicit topology (`T={A,Z}`) | App | Fig | Tbl | Equivalence link |
|---:|---|---|---|---|---|---|---|---|---|---|
| 50 | 3/2/0 | VA | V_A^1 | {50,54,75,79} | SSP | A-n1:R; n1-Z:R; n1-Z:L; n1-n2:R; n2-Z:L | 141/147 | 51/57 | 59/65 | Zobel |
| 51 | 3/2/0 | VA | V_A^1 | {51,55,76,80} | SSP | A-n1:R; n1-Z:R; n1-n2:L; n2-Z:R; n2-Z:L | 141/147 | 51/57 | 59/65 | Zobel |
| 52 | 3/2/0 | VA | V_A^1 | {52,56,77,81} | SSP | A-n1:R; n1-Z:L; n1-n2:R; n2-Z:R; n2-Z:L | 141/147 | 51/57 | 59/65 | Zobel |
| 53 | 3/2/0 | VB | V_B^1 | {53,57,78,82} | SP | A-n1:R; n1-n2:R; n1-n2:L; n2-Z:R; n2-Z:L | 142/148 | 51/57 | 59/65 | Zobel |
| 54 | 3/2/0 | VA | V_A^1 | {50,54,75,79} | SSP | A-Z:R; A-n1:R; n1-n2:L; n2-Z:R; n2-Z:L | 141/147 | 51/57 | 59/65 | Zobel |
| 55 | 3/2/0 | VA | V_A^1 | {51,55,76,80} | SSP | A-Z:R; A-n1:R; n1-Z:L; n1-n2:R; n2-Z:L | 141/147 | 51/57 | 59/65 | Zobel |
| 56 | 3/2/0 | VA | V_A^1 | {52,56,77,81} | SSP | A-Z:R; A-n1:L; n1-Z:R; n1-n2:R; n2-Z:L | 141/147 | 51/57 | 59/65 | Zobel |
| 57 | 3/2/0 | VB | V_B^2 | {53,57,78,82} | SP | A-Z:R; A-n1:R; n1-Z:L; A-n2:R; n2-Z:L | 142/148 | 51/57 | 59/65 | Zobel |
| 58 | 3/2/0 | VB | V_B^2 | {58,59,83,84} | SP | A-n1:R; n1-Z:L; A-n2:R; n2-Z:R; n2-Z:L | 142/148 | 51/57 | 59/65 | Zobel |
| 59 | 3/2/0 | VB | V_B^1 | {58,59,83,84} | SP | A-n1:R; A-n1:L; n1-Z:R; n1-n2:R; n2-Z:L | 142/148 | 51/57 | 59/65 | Zobel |
| 60 | 3/2/0 | VC | V_C^1 | {60,85} | bridge | A-n1:L; A-n2:R; n1-Z:R; n2-Z:R; n1-n2:L | 142/148 | 51/57 | 60/66 | none |
| 61 | 3/2/0 | VD | V_D^1 | {61,86} | bridge | A-n1:L; A-n2:R; n1-Z:R; n2-Z:L; n1-n2:R | 142/148 | 51/57 | 60/66 | none |
| 64 | 3/1/1 | VE | V_E^2 | {64,67,89,92} | SSP | A-n1:R; n1-Z:R; n1-n2:L; n2-Z:R; n2-Z:C | 143/149 | 51/57 | 60/66 | Zobel |
| 65 | 3/1/1 | VE | V_E^2 | {65,68,91,93} | SSP | A-Z:R; A-n1:L; n1-n2:R; n2-Z:R; n2-Z:C | 143/149 | 51/57 | 60/66 | Zobel |
| 66 | 3/1/1 | VE | V_E^2 | {66,69,90,94} | SSP | A-Z:R; A-n1:L; n1-Z:R; n1-n2:R; n2-Z:C | 143/149 | 51/57 | 60/66 | Zobel |
| 67 | 3/1/1 | VE | V_E^1 | {64,67,89,92} | SSP | A-Z:R; A-n1:R; n1-Z:L; n1-n2:R; n2-Z:C | 143/149 | 51/57 | 60/66 | Zobel |
| 68 | 3/1/1 | VE | V_E^1 | {65,68,91,93} | SSP | A-n1:R; n1-Z:R; n1-n2:R; n2-Z:C; n1-Z:L | 143/149 | 51/57 | 60/66 | Zobel |
| 69 | 3/1/1 | VE | V_E^1 | {66,69,90,94} | SSP | A-n1:R; n1-Z:L; n1-n2:R; n2-Z:R; n2-Z:C | 143/149 | 51/57 | 60/66 | Zobel |
| 70 | 3/1/1 | VH | V_H^1 | {70,95} | bridge | A-n1:L; A-n2:R; n1-Z:R; n2-Z:R; n1-n2:C | 144/150 | 51/57 | 61/67 | none |
| 75 | 3/0/2 | VA | V_A^2 | {50,54,75,79} | SSP | A-Z:R; A-n1:R; n1-n2:C; n2-Z:R; n2-Z:C | 141/147 | 51/57 | 59/65 | Zobel |
| 76 | 3/0/2 | VA | V_A^2 | {51,55,76,80} | SSP | A-Z:R; A-n1:R; n1-Z:C; n1-n2:R; n2-Z:C | 141/147 | 51/57 | 59/65 | Zobel |
| 77 | 3/0/2 | VA | V_A^2 | {52,56,77,81} | SSP | A-Z:R; A-n1:C; n1-Z:R; n1-n2:R; n2-Z:C | 141/147 | 51/57 | 59/65 | Zobel |
| 78 | 3/0/2 | VB | V_B^4 | {53,57,78,82} | SP | A-Z:R; A-n1:R; n1-Z:C; A-n2:C; n2-Z:R | 142/148 | 51/57 | 59/65 | Zobel |
| 79 | 3/0/2 | VA | V_A^2 | {50,54,75,79} | SSP | A-n1:R; n1-Z:R; n1-n2:R; n2-Z:C; n1-Z:C | 141/147 | 51/57 | 59/65 | Zobel |
| 80 | 3/0/2 | VA | V_A^2 | {51,55,76,80} | SSP | A-n1:R; n1-Z:R; n1-n2:C; n2-Z:R; n2-Z:C | 141/147 | 51/57 | 59/65 | Zobel |
| 81 | 3/0/2 | VA | V_A^2 | {52,56,77,81} | SSP | A-n1:R; n1-Z:C; n1-n2:R; n2-Z:R; n2-Z:C | 141/147 | 51/57 | 59/65 | Zobel |
| 82 | 3/0/2 | VB | V_B^3 | {53,57,78,82} | SP | A-n1:R; n1-n2:R; n1-n2:C; n2-Z:R; n2-Z:C | 142/148 | 51/57 | 59/65 | Zobel |
| 83 | 3/0/2 | VB | V_B^3 | {58,59,83,84} | SP | A-n1:R; A-n1:C; n1-Z:R; n1-n2:R; n2-Z:C | 142/148 | 51/57 | 59/65 | Zobel |
| 84 | 3/0/2 | VB | V_B^4 | {58,59,83,84} | SP | A-n1:C; n1-Z:R; A-n2:R; n2-Z:R; n2-Z:C | 142/148 | 51/57 | 59/65 | Zobel |
| 85 | 3/0/2 | VC | V_C^2 | {60,85} | bridge | A-n1:R; A-n2:C; n1-Z:R; n2-Z:R; n1-n2:C | 142/148 | 51/57 | 60/66 | none |
| 86 | 3/0/2 | VD | V_D^2 | {61,86} | bridge | A-n1:C; A-n2:R; n1-Z:R; n2-Z:C; n1-n2:R | 142/148 | 51/57 | 60/66 | none |
| 89 | 3/1/1 | VE | V_E^4 | {64,67,89,92} | SSP | A-n1:R; n1-Z:R; n1-n2:C; n2-Z:R; n2-Z:L | 143/149 | 51/57 | 60/66 | Zobel |
| 90 | 3/1/1 | VE | V_E^4 | {66,69,90,94} | SSP | A-Z:R; A-n1:C; n1-Z:R; n1-n2:R; n2-Z:L | 143/149 | 51/57 | 60/66 | Zobel |
| 91 | 3/1/1 | VE | V_E^4 | {65,68,91,93} | SSP | A-Z:R; A-n1:R; n1-n2:C; n2-Z:R; n2-Z:L | 143/149 | 51/57 | 60/66 | Zobel |
| 92 | 3/1/1 | VE | V_E^3 | {64,67,89,92} | SSP | A-Z:R; A-n1:R; n1-Z:C; n1-n2:R; n2-Z:L | 143/149 | 51/57 | 60/66 | Zobel |
| 93 | 3/1/1 | VE | V_E^3 | {65,68,91,93} | SSP | A-n1:R; n1-Z:R; n1-n2:R; n2-Z:L; n1-Z:C | 143/149 | 51/57 | 60/66 | Zobel |
| 94 | 3/1/1 | VE | V_E^3 | {66,69,90,94} | SSP | A-n1:R; n1-Z:C; n1-n2:R; n2-Z:R; n2-Z:L | 143/149 | 51/57 | 60/66 | Zobel |
| 95 | 3/1/1 | VH | V_H^2 | {70,95} | bridge | A-n1:C; A-n2:R; n1-Z:R; n2-Z:R; n1-n2:L | 144/150 | 51/57 | 61/67 | none |
| 98 | 3/1/1 | VF | V_F^2 | {98,101} | SP | A-n1:R; n1-n2:R; n1-n2:C; n2-Z:R; n2-Z:L | 144/150 | 51/57 | 60/66 | Zobel |
| 99 | 3/1/1 | VF | V_F^2 | {99,100,102,103} | SP | A-n1:R; A-n1:L; n1-Z:R; n1-n2:R; n2-Z:C | 144/150 | 51/57 | 60/66 | Zobel |
| 100 | 3/1/1 | VF | V_F^2 | {99,100,102,103} | SP | A-n1:R; A-n1:C; n1-Z:R; n1-n2:R; n2-Z:L | 144/150 | 51/57 | 60/66 | Zobel |
| 101 | 3/1/1 | VF | V_F^1 | {98,101} | SP | A-Z:R; A-n1:R; n1-Z:L; A-n2:R; n2-Z:C | 144/150 | 51/57 | 60/66 | Zobel |
| 102 | 3/1/1 | VF | V_F^1 | {99,100,102,103} | SP | A-n1:R; n1-Z:L; A-n2:R; n2-Z:R; n2-Z:C | 144/150 | 51/57 | 60/66 | Zobel |
| 103 | 3/1/1 | VF | V_F^1 | {99,100,102,103} | SP | A-n1:C; n1-Z:R; A-n2:R; n2-Z:R; n2-Z:L | 144/150 | 51/57 | 60/66 | Zobel |
| 104 | 3/1/1 | VG | V_G^1 | {104,106} | SP / bridge | A-n1:R; n1-n2:R; n2-Z:L; n1-n3:R; n3-Z:C | 144/150 | 51/57 | 60/66 | Y-delta to 105 |
| 105 | 3/1/1 | VG | V_G^1 | {105,107} | SP / bridge | A-n1:R; A-n2:R; n1-Z:L; n2-Z:C; n1-n2:R | 144/150 | 51/57 | 60/66 | Y-delta to 104 |
| 106 | 3/1/1 | VG | V_G^2 | {104,106} | SP / bridge | A-Z:R; A-n1:R; A-n1:C; n1-Z:R; n1-Z:L | 144/150 | 51/57 | 60/66 | Y-delta to 107 |
| 107 | 3/1/1 | VG | V_G^2 | {105,107} | SP / bridge | A-n1:C; A-n2:R; n1-Z:L; n2-Z:R; n1-n2:R | 144/150 | 51/57 | 60/66 | Y-delta to 106 |
| 108 | 3/1/1 | VI | V_I | {108} | bridge | A-n1:C; A-n2:R; n1-Z:R; n2-Z:L; n1-n2:R | 144/150 | 51/57 | 61/67 | none |

## 5. Independently derived RICE matches

Each source topology above was independently encoded as a
`PrimitiveNetwork`, then compared with all 148 committed catalogue rows under
`colour-preserving-port-augmented-cycle-matroid-v1`. Descriptor text and list
order were not matching predicates. `Card.` is the signature-match
cardinality; every production disposition shown here records the historical
evidence-only milestone, when all 49 subjects were `unresolved`.

| No. | Fixture | RICE catalogue ID | Representative descriptor | R/L/C | Relation | Card. | Disposition | Evidence locator |
|---:|---|---|---|---|---|---:|---|---|
| 50 | ms-c108-five-50 | lh148-18bfb3d8c33bbf58 | `0-2:L;0-2:R;0-3:L;1-2:R;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 51 | ms-c108-five-51 | lh148-3ae4767397da2b12 | `0-2:L;0-2:R;0-3:R;1-3:R;2-3:L` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 52 | ms-c108-five-52 | lh148-3a5b171b0d2af32a | `0-2:L;0-2:R;0-3:L;1-3:R;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 53 | ms-c108-five-53 | lh148-4e1e2e1aa376f921 | `0-2:L;0-2:R;1-3:L;1-3:R;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 54 | ms-c108-five-54 | lh148-1928fc6c03828cba | `0-1:R;0-2:L;0-2:R;1-3:L;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 55 | ms-c108-five-55 | lh148-ceda8e624931aa86 | `0-1:R;0-2:L;0-3:L;1-2:R;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 56 | ms-c108-five-56 | lh148-44baa015c7dbccf2 | `0-1:R;0-2:L;0-3:R;1-3:L;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 57 | ms-c108-five-57 | lh148-369eb555ae634258 | `0-1:R;0-2:L;0-3:L;1-2:R;1-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 58 | ms-c108-five-58 | lh148-44371b2082f84fcf | `0-2:L;0-2:R;0-3:L;1-2:R;1-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 59 | ms-c108-five-59 | lh148-a33c22b118699e51 | `0-2:L;0-2:R;1-2:R;1-3:L;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 60 | ms-c108-five-60 | lh148-2f4c974bc7831e4a | `0-2:L;0-3:R;1-2:R;1-3:R;2-3:L` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 61 | ms-c108-five-61 | lh148-c27124d195b882ef | `0-2:L;0-3:R;1-2:R;1-3:L;2-3:R` | 3/2/0 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 64 | ms-c108-five-64 | lh148-66a0391fd4dc6879 | `0-2:C;0-2:R;0-3:R;1-3:R;2-3:L` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 65 | ms-c108-five-65 | lh148-8324b82e90bde552 | `0-1:R;0-2:C;0-2:R;1-3:L;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 66 | ms-c108-five-66 | lh148-6456494eb91d8897 | `0-1:R;0-2:C;0-3:R;1-3:L;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 67 | ms-c108-five-67 | lh148-e965ee7277ab24b2 | `0-1:R;0-2:C;0-3:L;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 68 | ms-c108-five-68 | lh148-6bd2964e8fab676a | `0-2:C;0-3:L;0-3:R;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 69 | ms-c108-five-69 | lh148-e5953a9cf3d9cfa6 | `0-2:C;0-2:R;0-3:L;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 70 | ms-c108-five-70 | lh148-1ea888a6b965ac39 | `0-2:L;0-3:R;1-2:R;1-3:R;2-3:C` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 75 | ms-c108-five-75 | lh148-e7e64ac1f0778b53 | `0-1:R;0-2:C;0-2:R;1-3:C;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 76 | ms-c108-five-76 | lh148-0c94f62def7dc462 | `0-1:R;0-2:C;0-3:C;1-2:R;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 77 | ms-c108-five-77 | lh148-90a706c48f568ac5 | `0-1:R;0-2:C;0-3:R;1-3:C;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 78 | ms-c108-five-78 | lh148-3398b6c5b497ac1f | `0-1:R;0-2:C;0-3:C;1-2:R;1-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 79 | ms-c108-five-79 | lh148-5c71fb151bc82017 | `0-2:C;0-2:R;0-3:C;1-2:R;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 80 | ms-c108-five-80 | lh148-a99495648823d8f1 | `0-2:C;0-2:R;0-3:R;1-3:R;2-3:C` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 81 | ms-c108-five-81 | lh148-0d78e9c38dc5b94e | `0-2:C;0-2:R;0-3:C;1-3:R;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 82 | ms-c108-five-82 | lh148-5af86517070376b6 | `0-2:C;0-2:R;1-3:C;1-3:R;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 83 | ms-c108-five-83 | lh148-f54f327274744e9f | `0-2:C;0-2:R;1-2:R;1-3:C;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 84 | ms-c108-five-84 | lh148-cd4b770f5478f872 | `0-2:C;0-2:R;0-3:C;1-2:R;1-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 85 | ms-c108-five-85 | lh148-9c9bca1b4c7a5c48 | `0-2:C;0-3:R;1-2:R;1-3:R;2-3:C` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 86 | ms-c108-five-86 | lh148-5d2f2ceb56fb8299 | `0-2:C;0-3:R;1-2:R;1-3:C;2-3:R` | 3/0/2 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 89 | ms-c108-five-89 | lh148-6601ce95cb4866ea | `0-2:C;0-3:R;1-3:R;2-3:L;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 90 | ms-c108-five-90 | lh148-d640e5a51b7f9267 | `0-1:R;0-2:C;1-2:R;1-3:L;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 91 | ms-c108-five-91 | lh148-7f69006023a9ba91 | `0-1:R;0-2:C;1-3:L;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 92 | ms-c108-five-92 | lh148-d83685d4a7f0cd41 | `0-1:R;0-2:C;0-3:L;1-2:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 93 | ms-c108-five-93 | lh148-cd27971291cfaf9a | `0-2:C;0-2:R;0-3:L;1-2:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 94 | ms-c108-five-94 | lh148-75a667eae30e9bd2 | `0-2:C;0-3:L;0-3:R;1-2:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 95 | ms-c108-five-95 | lh148-6ce044778ba295df | `0-2:C;0-3:R;1-2:R;1-3:R;2-3:L` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 98 | ms-c108-five-98 | lh148-ce4e4bbc3cb5bc7b | `0-2:C;0-2:R;1-3:L;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 99 | ms-c108-five-99 | lh148-ee8c722fe8f18278 | `0-2:C;0-3:R;1-3:L;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 100 | ms-c108-five-100 | lh148-061515c41719c7cc | `0-2:C;0-2:R;1-2:R;1-3:L;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 101 | ms-c108-five-101 | lh148-1c63245475d83fd7 | `0-1:R;0-2:C;0-3:L;1-2:R;1-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 102 | ms-c108-five-102 | lh148-d7f4be8bd126187c | `0-2:C;0-2:R;0-3:L;1-2:R;1-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 103 | ms-c108-five-103 | lh148-4b5da2aa5cfac0cc | `0-2:C;0-3:L;0-3:R;1-2:R;1-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 104 | ms-c108-five-104 | lh148-539216b2b01390c9 | `0-2:C;0-3:L;1-4:R;2-4:R;3-4:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 105 | ms-c108-five-105 | lh148-4ce178b19ddf0bc8 | `0-2:C;0-3:L;1-2:R;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 106 | ms-c108-five-106 | lh148-0d128fdfe5562143 | `0-1:R;0-2:C;0-2:R;1-2:L;1-2:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 107 | ms-c108-five-107 | lh148-226210ea8617797f | `0-2:C;0-3:R;1-2:L;1-3:R;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |
| 108 | ms-c108-five-108 | lh148-11e619a8865be381 | `0-2:C;0-3:R;1-2:R;1-3:L;2-3:R` | 3/1/1 | colour-preserving-port-augmented-cycle-matroid-v1 | 1 | unresolved | this report, section 4 |

At the evidence-only milestone, the 49 IDs were distinct and exhausted the
unresolved population. The union with the 25 applied low-order and 34 applied
four-element identities had
108 distinct canonical numbers and 108 distinct nonexcluded RICE subjects,
exactly the nonexcluded side of the 148-row catalogue. The later complete
application now applies all 108 identities without changing that structural
coverage result.

## 6. Reduction-target and historical-identity separation

The matching computation uses only each numbered Appendix D diagram's explicit
fixture. It does not consume any `reduction-target-match`, conditional target,
Zobel destination, or earlier exclusion mapping. A statement that an excluded
subject reduces to a numbered network does not make the excluded subject that
network and does not identify the target's RICE row. At the evidence-only
milestone, none of the 49 matched subjects was excluded or carried a historical
identifier. The later complete five-element application assigns each subject
its exact cross-checked `morelli-smith-canonical-network` identifier.

The complete source-class arithmetic is now 21 low-order classes plus 20
four-element classes plus 21 five-element classes, or 62. That is complete
source-label transcription, not an independent RICE reproduction of 62
realizability sets. Structural matching establishes network identity only.

## 7. Previous-workspace audit

This bounded audit was performed only after the authoritative transcription and
RICE matching were complete. The sibling repositories were read-only and clean
at `network-theory` commit `87b831831c154c5c3675853a99ff7e5a2b7dfb6d`,
`pynntt` commit `f3db06032cbe23d583d77f6cb79d21ced90d7651`, and
`pynntt_lab` commit `1ddd90034da4594bb6a3728b0700918883fd1172`.

The `network-theory` directory
`016--graph-generation/doc/ladenheim-catalogue/ladenheim-schematics/` contains
numbered PNGs for the five-element numbers. A bounded visual sample of networks
50, 60, 70, 104, and 108 agrees with the independent Appendix D transcription.
The `pynntt` CSV `catalogues/2019--MS-network-descriptors.csv` has 108 numbered
descriptor rows, but it was not used for topology, numbering, class, orbit, or
RICE-ID allocation. No sibling record supplied any conclusion in this report.

## 8. Conclusions and limitations

The authoritative inventory is 49 five-element networks in nine subfamilies,
21 equivalence classes, and 16 group-action orbits. The 49 independently
transcribed fixtures select 49 distinct unique RICE subjects and, at the
evidence-only milestone, exhausted the unresolved production population.
Together with the prior 59 reviewed identities, they provide evidence-level
coverage of all canonical 108 numbers and all 108 nonexcluded RICE subjects.

At the report milestone the 49 mappings were evidence-only and unresolved. The
subsequent format-version-6 group encoded them, and the later complete
application now retains and numbers all 49 subjects. Current production is 40
excluded, 0 unresolved, and 108 retained. The historical unresolved-state
checks below remain pinned to the accepted evidence revision, and the durable
structural-match result is unchanged. Neither the report nor the application
independently reproduces the source realizability classes or begins the
108-to-62 production classification.

## 9. Historical reproduction commands

This block reproduces the accepted evidence-only revision and is not intended
to run against current main. Prepare a detached worktree at
`b64946fd9ddcae6f764921d082b315affb9e233e`; this leaves the current checkout
and branch untouched. The symlink reuses the current repository's virtual
environment, while `PYTHONPATH` selects the pinned worktree's source:

```bash
repo_root="$(git rev-parse --show-toplevel)"
repro_parent="$(mktemp -d)"
repro_dir="$repro_parent/rice"
git -C "$repo_root" worktree add --detach \
    "$repro_dir" \
    b64946fd9ddcae6f764921d082b315affb9e233e
ln -s "$repo_root/.venv" "$repro_dir/.venv"
export PYTHONPATH="$repro_dir/src"
cd "$repro_dir"
```

Run the existing Python block there. It reads the explicit fixture and
expected-match tables above, constructs primitive coloured networks, scans all
148 catalogue rows, and verifies the authoritative inventory, unique matches,
historical production boundary, and full 108-subject union.

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

REPORT = Path(
    "docs/comparisons/ladenheim-canonical-108-five-element-evidence.md"
)
RELATION = "colour-preserving-port-augmented-cycle-matroid-v1"
EXPECTED_NUMBERS = {
    50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
    64, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79,
    80, 81, 82, 83, 84, 85, 86, 89, 90, 91, 92, 93,
    94, 95, 98, 99, 100, 101, 102, 103, 104, 105, 106,
    107, 108,
}
EXPECTED_SUBFAMILIES = {
    "VA": (12, 2, 3), "VB": (8, 4, 2), "VC": (2, 2, 1),
    "VD": (2, 2, 1), "VE": (12, 4, 3), "VF": (6, 2, 2),
    "VG": (4, 2, 2), "VH": (2, 2, 1), "VI": (1, 1, 1),
}


def table_rows(text, heading):
    section = text.split(heading, 1)[1].split("\n## ", 1)[0]
    rows = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0].isdigit():
            rows.append(cells)
    return rows


text = REPORT.read_text()
source_rows = table_rows(text, "## 4. Authoritative source transcription")
match_rows = table_rows(text, "## 5. Independently derived RICE matches")
assert len(source_rows) == len(match_rows) == 49

source = {}
for cells in source_rows:
    number = int(cells[0])
    inventory = tuple(int(value) for value in cells[1].split("/"))
    orbit = tuple(int(value) for value in cells[4].strip("{}").split(","))
    edges = []
    for item in cells[6].split(";"):
        endpoints, kind = item.strip().split(":")
        left, right = endpoints.split("-")
        edges.append(PrimitiveEdge(left, right, kind))
    source[number] = {
        "inventory": inventory,
        "subfamily": cells[2],
        "class": cells[3],
        "orbit": orbit,
        "fixture": PrimitiveNetwork(("A", "Z"), tuple(edges)),
    }

expected_matches = {}
for cells in match_rows:
    number = int(cells[0])
    expected_matches[number] = {
        "fixture_id": cells[1],
        "catalogue_id": cells[2],
        "descriptor": cells[3].strip("`"),
        "inventory": tuple(int(value) for value in cells[4].split("/")),
        "relation": cells[5],
        "cardinality": int(cells[6]),
        "disposition": cells[7],
    }

assert set(source) == set(expected_matches) == EXPECTED_NUMBERS
assert len({row["fixture_id"] for row in expected_matches.values()}) == 49
assert all(
    row["fixture_id"] == f"ms-c108-five-{number}"
    for number, row in expected_matches.items()
)

for subfamily, (networks, classes, orbits) in EXPECTED_SUBFAMILIES.items():
    members = [row for row in source.values() if row["subfamily"] == subfamily]
    assert len(members) == networks
    assert len({row["class"] for row in members}) == classes
    assert len({row["orbit"] for row in members}) == orbits
assert sum(value[0] for value in EXPECTED_SUBFAMILIES.values()) == 49
assert sum(value[1] for value in EXPECTED_SUBFAMILIES.values()) == 21
assert sum(value[2] for value in EXPECTED_SUBFAMILIES.values()) == 16
assert Counter(row["inventory"] for row in source.values()) == {
    (3, 2, 0): 12, (3, 0, 2): 12, (3, 1, 1): 25,
}

catalogue = json.loads(Path("data/counts/ladenheim-148.json").read_text())
ledger = json.loads(
    Path("data/comparisons/ladenheim-148-to-108.json").read_text()
)
assert len(catalogue["records"]) == len(ledger["records"]) == 148
assert ledger["summary"]["by_proposed_disposition"] == {
    "exclude": 40, "retain": 59, "unresolved": 49,
}
assert all(row["basic_graph_assignment"] is None for row in ledger["records"])
ledger_rows = {row["catalogue_id"]: row for row in ledger["records"]}
identifier_rows = [row for row in ledger["records"] if row["historical_identifiers"]]
assert len(identifier_rows) == 59
assert all(len(row["historical_identifiers"]) == 1 for row in identifier_rows)
applied_numbers = {
    row["historical_identifiers"][0]["value"] for row in identifier_rows
}
applied_subjects = {row["catalogue_id"] for row in identifier_rows}
assert len(applied_numbers) == len(applied_subjects) == 59

catalogue_by_signature = {}
for row in catalogue["records"]:
    signature = canonical_structural_signature(
        network_from_descriptor(row["representative_descriptor"])
    )
    assert signature.relation == RELATION
    catalogue_by_signature.setdefault(signature, []).append(row)

matches = {}
for number in sorted(source):
    metadata = source[number]
    fixture = metadata["fixture"]
    signature = canonical_structural_signature(fixture)
    assert signature.relation == RELATION
    rows = catalogue_by_signature.get(signature, [])
    assert len(rows) == 1, (number, [row["catalogue_id"] for row in rows])
    row = rows[0]
    expected = expected_matches[number]
    assert expected["relation"] == RELATION
    assert expected["cardinality"] == 1
    assert fixture.counts == metadata["inventory"] == expected["inventory"]
    assert (row["r"], row["l"], row["c"]) == metadata["inventory"]
    assert row["rlc"] == 5 and row["r"] == 3
    assert row["catalogue_id"] == expected["catalogue_id"]
    assert row["representative_descriptor"] == expected["descriptor"]
    production_row = ledger_rows[row["catalogue_id"]]
    assert production_row["proposed_disposition"] == expected["disposition"]
    assert production_row["comparison_status"] == "unresolved"
    assert production_row["historical_identifiers"] == []
    matches[number] = row
    print(
        f"network {number:>3} {metadata['subfamily']} {metadata['class']} -> "
        f"{row['catalogue_id']} {row['representative_descriptor']}"
    )

matched_subjects = {row["catalogue_id"] for row in matches.values()}
assert len(matches) == len(matched_subjects) == 49
unresolved_subjects = {
    row["catalogue_id"] for row in ledger["records"]
    if row["proposed_disposition"] == "unresolved"
}
excluded_subjects = {
    row["catalogue_id"] for row in ledger["records"]
    if row["proposed_disposition"] == "exclude"
}
assert matched_subjects == unresolved_subjects
assert not (matched_subjects & excluded_subjects)
assert not (matched_subjects & applied_subjects)
assert all(ledger_rows[subject]["rlc"] == 5 for subject in unresolved_subjects)
assert applied_numbers.isdisjoint(EXPECTED_NUMBERS)
assert len(applied_numbers | EXPECTED_NUMBERS) == 108
assert len(applied_subjects | matched_subjects) == 108
assert applied_subjects | matched_subjects == (
    set(ledger_rows) - excluded_subjects
)

print("source inventory: 49 networks; 9 subfamilies; 21 classes; 16 orbits")
print("component inventories: R3/L2/C0=12; R3/L0/C2=12; R3/L1/C1=25")
print("structural matches: 49 distinct unique unresolved RICE subjects")
print("canonical union: 108 distinct numbers; 108 distinct nonexcluded subjects")
print("production unchanged: 40 excluded / 49 unresolved / 59 retained")
print("identifiers: 59 populated rows; graph assignments: 148 null")
PY
```

## 10. Observed reproduction output

The exact output observed from the block above was:

```text
network  50 VA V_A^1 -> lh148-18bfb3d8c33bbf58 0-2:L;0-2:R;0-3:L;1-2:R;2-3:R
network  51 VA V_A^1 -> lh148-3ae4767397da2b12 0-2:L;0-2:R;0-3:R;1-3:R;2-3:L
network  52 VA V_A^1 -> lh148-3a5b171b0d2af32a 0-2:L;0-2:R;0-3:L;1-3:R;2-3:R
network  53 VB V_B^1 -> lh148-4e1e2e1aa376f921 0-2:L;0-2:R;1-3:L;1-3:R;2-3:R
network  54 VA V_A^1 -> lh148-1928fc6c03828cba 0-1:R;0-2:L;0-2:R;1-3:L;2-3:R
network  55 VA V_A^1 -> lh148-ceda8e624931aa86 0-1:R;0-2:L;0-3:L;1-2:R;2-3:R
network  56 VA V_A^1 -> lh148-44baa015c7dbccf2 0-1:R;0-2:L;0-3:R;1-3:L;2-3:R
network  57 VB V_B^2 -> lh148-369eb555ae634258 0-1:R;0-2:L;0-3:L;1-2:R;1-3:R
network  58 VB V_B^2 -> lh148-44371b2082f84fcf 0-2:L;0-2:R;0-3:L;1-2:R;1-3:R
network  59 VB V_B^1 -> lh148-a33c22b118699e51 0-2:L;0-2:R;1-2:R;1-3:L;2-3:R
network  60 VC V_C^1 -> lh148-2f4c974bc7831e4a 0-2:L;0-3:R;1-2:R;1-3:R;2-3:L
network  61 VD V_D^1 -> lh148-c27124d195b882ef 0-2:L;0-3:R;1-2:R;1-3:L;2-3:R
network  64 VE V_E^2 -> lh148-66a0391fd4dc6879 0-2:C;0-2:R;0-3:R;1-3:R;2-3:L
network  65 VE V_E^2 -> lh148-8324b82e90bde552 0-1:R;0-2:C;0-2:R;1-3:L;2-3:R
network  66 VE V_E^2 -> lh148-6456494eb91d8897 0-1:R;0-2:C;0-3:R;1-3:L;2-3:R
network  67 VE V_E^1 -> lh148-e965ee7277ab24b2 0-1:R;0-2:C;0-3:L;1-3:R;2-3:R
network  68 VE V_E^1 -> lh148-6bd2964e8fab676a 0-2:C;0-3:L;0-3:R;1-3:R;2-3:R
network  69 VE V_E^1 -> lh148-e5953a9cf3d9cfa6 0-2:C;0-2:R;0-3:L;1-3:R;2-3:R
network  70 VH V_H^1 -> lh148-1ea888a6b965ac39 0-2:L;0-3:R;1-2:R;1-3:R;2-3:C
network  75 VA V_A^2 -> lh148-e7e64ac1f0778b53 0-1:R;0-2:C;0-2:R;1-3:C;2-3:R
network  76 VA V_A^2 -> lh148-0c94f62def7dc462 0-1:R;0-2:C;0-3:C;1-2:R;2-3:R
network  77 VA V_A^2 -> lh148-90a706c48f568ac5 0-1:R;0-2:C;0-3:R;1-3:C;2-3:R
network  78 VB V_B^4 -> lh148-3398b6c5b497ac1f 0-1:R;0-2:C;0-3:C;1-2:R;1-3:R
network  79 VA V_A^2 -> lh148-5c71fb151bc82017 0-2:C;0-2:R;0-3:C;1-2:R;2-3:R
network  80 VA V_A^2 -> lh148-a99495648823d8f1 0-2:C;0-2:R;0-3:R;1-3:R;2-3:C
network  81 VA V_A^2 -> lh148-0d78e9c38dc5b94e 0-2:C;0-2:R;0-3:C;1-3:R;2-3:R
network  82 VB V_B^3 -> lh148-5af86517070376b6 0-2:C;0-2:R;1-3:C;1-3:R;2-3:R
network  83 VB V_B^3 -> lh148-f54f327274744e9f 0-2:C;0-2:R;1-2:R;1-3:C;2-3:R
network  84 VB V_B^4 -> lh148-cd4b770f5478f872 0-2:C;0-2:R;0-3:C;1-2:R;1-3:R
network  85 VC V_C^2 -> lh148-9c9bca1b4c7a5c48 0-2:C;0-3:R;1-2:R;1-3:R;2-3:C
network  86 VD V_D^2 -> lh148-5d2f2ceb56fb8299 0-2:C;0-3:R;1-2:R;1-3:C;2-3:R
network  89 VE V_E^4 -> lh148-6601ce95cb4866ea 0-2:C;0-3:R;1-3:R;2-3:L;2-3:R
network  90 VE V_E^4 -> lh148-d640e5a51b7f9267 0-1:R;0-2:C;1-2:R;1-3:L;2-3:R
network  91 VE V_E^4 -> lh148-7f69006023a9ba91 0-1:R;0-2:C;1-3:L;1-3:R;2-3:R
network  92 VE V_E^3 -> lh148-d83685d4a7f0cd41 0-1:R;0-2:C;0-3:L;1-2:R;2-3:R
network  93 VE V_E^3 -> lh148-cd27971291cfaf9a 0-2:C;0-2:R;0-3:L;1-2:R;2-3:R
network  94 VE V_E^3 -> lh148-75a667eae30e9bd2 0-2:C;0-3:L;0-3:R;1-2:R;2-3:R
network  95 VH V_H^2 -> lh148-6ce044778ba295df 0-2:C;0-3:R;1-2:R;1-3:R;2-3:L
network  98 VF V_F^2 -> lh148-ce4e4bbc3cb5bc7b 0-2:C;0-2:R;1-3:L;1-3:R;2-3:R
network  99 VF V_F^2 -> lh148-ee8c722fe8f18278 0-2:C;0-3:R;1-3:L;1-3:R;2-3:R
network 100 VF V_F^2 -> lh148-061515c41719c7cc 0-2:C;0-2:R;1-2:R;1-3:L;2-3:R
network 101 VF V_F^1 -> lh148-1c63245475d83fd7 0-1:R;0-2:C;0-3:L;1-2:R;1-3:R
network 102 VF V_F^1 -> lh148-d7f4be8bd126187c 0-2:C;0-2:R;0-3:L;1-2:R;1-3:R
network 103 VF V_F^1 -> lh148-4b5da2aa5cfac0cc 0-2:C;0-3:L;0-3:R;1-2:R;1-3:R
network 104 VG V_G^1 -> lh148-539216b2b01390c9 0-2:C;0-3:L;1-4:R;2-4:R;3-4:R
network 105 VG V_G^1 -> lh148-4ce178b19ddf0bc8 0-2:C;0-3:L;1-2:R;1-3:R;2-3:R
network 106 VG V_G^2 -> lh148-0d128fdfe5562143 0-1:R;0-2:C;0-2:R;1-2:L;1-2:R
network 107 VG V_G^2 -> lh148-226210ea8617797f 0-2:C;0-3:R;1-2:L;1-3:R;2-3:R
network 108 VI V_I -> lh148-11e619a8865be381 0-2:C;0-3:R;1-2:R;1-3:L;2-3:R
source inventory: 49 networks; 9 subfamilies; 21 classes; 16 orbits
component inventories: R3/L2/C0=12; R3/L0/C2=12; R3/L1/C1=25
structural matches: 49 distinct unique unresolved RICE subjects
canonical union: 108 distinct numbers; 108 distinct nonexcluded subjects
production unchanged: 40 excluded / 49 unresolved / 59 retained
identifiers: 59 populated rows; graph assignments: 148 null
```

After recording the result, remove the detached worktree without changing the
current checkout:

```bash
cd "$repo_root"
unlink "$repro_dir/.venv"
git worktree remove "$repro_dir"
rmdir "$repro_parent"
```

The current canonical-identity contract, generator, and tests separately
validate the later 40 excluded / 0 unresolved / 108 retained production state.
