# Evidence for the four-element canonical Ladenheim networks

## 1. Purpose and production boundary

This report transcribes and independently matches the complete four-element
portion of the canonical 108-network catalogue in A. Morelli and M. C. Smith,
*Passive Network Synthesis: An Approach to Classification* (SIAM, 2019).
As originally accepted, it was evidence only: it did not add structured
annotation evidence, apply a retained disposition, populate a historical
identifier or graph assignment, or begin the five-element or 108-to-62 work.

At that evidence-only milestone, production remained 40 excluded, 83
unresolved, and 25 retained records. The existing 25 retained low-order
identities were unchanged. Exactly
25 historical-identifier lists remain populated with those low-order canonical
identifiers, the other 123 lists remain empty, and every
`basic_graph_assignment` remains null.

The subsequent format-version-6 contract milestone encodes all 34 reviewed
mappings as one controlled canonical-identity evidence group, including their
authoritative definitions, subject-bound matches, aggregate inventory, and
pinned computation. None of the 34 mappings is applied in production: all 34
subjects remain unresolved, production remains 40 excluded, 83 unresolved,
and 25 retained, and a later application requires a separate pull request. The
original reproduction below remains pinned to accepted revision
`b499f0340771feaacb535fb987a45754dbeb050e`.

## 2. Source identity and exact locators

The inspected PDF was the existing read-only copy at
`../pynntt_lab/ref/2019--Morelli-and-Smith--Passive_Network_Synthesis_An_Approach_to_Classification.pdf`.
Its SHA-256 is
`29018f24a0316b984b76b6868a2c425309df7085ad1df8ca83d17c304704a2f8`.
It was not copied into RICE.

| Material | Printed page | Zero-based PDF index | Evidence used |
|---|---:|---:|---|
| Table 6.2 | 49 | 55 | four-element network, orbit, and equivalence-class counts by subfamily |
| Figure 6.2 | 50 | 56 | canonical numbers, exact orbit connections, class shading and labels, `p`/`s` arrows, and dashed Zobel links |
| Table 6.11, four-element rows | 58--59 | 64--65 | equivalence-class labels and member network numbers |
| Appendix D, subfamily IVA | 138 | 144 | rendered primitive circuit diagrams |
| Appendix D, subfamilies IVB and IVC | 139 | 145 | rendered primitive circuit diagrams |
| Appendix D, subfamilies IVD, IVE, and IVF | 140 | 146 | rendered primitive circuit diagrams |

All topologies and port placements were transcribed from rendered Appendix D
pages. Figure 6.2 was rendered before its solid orbit connections, shaded
equivalence classes, and dashed Zobel links were recorded. Extracted text was
used only to locate and cross-check labels and counts.

## 3. Source terminology and aggregate inventory

A canonical network number identifies one rendered coloured two-terminal
diagram. An equivalence class groups networks with the source's same
realizability set; Figure 6.2 shows multi-network classes with shaded dashed
Zobel links. A group-action orbit is instead the set connected by the solid
`p` and `s` actions. A subfamily can contain several orbits and several
equivalence classes, so subfamily membership proves neither identity nor
realizability-set equivalence.

Table 6.2 gives the complete four-element inventory:

| Subfamily | Networks | Equivalence classes | Orbits |
|---|---:|---:|---:|
| IVA | 12 | 4 | 3 |
| IVB | 4 | 4 | 1 |
| IVC | 8 | 4 | 2 |
| IVD | 4 | 2 | 2 |
| IVE | 4 | 4 | 1 |
| IVF | 2 | 2 | 1 |
| **Total** | **34** | **20** | **10** |

The exact orbit member sets read from the solid Figure 6.2 connections are:

- IVA: `{37, 30, 45, 22}`, `{35, 28, 43, 20}`, and
  `{36, 29, 44, 21}`;
- IVB: `{38, 31, 46, 23}`;
- IVC: `{40, 33, 48, 24}` and `{39, 32, 47, 25}`;
- IVD: `{72, 73}` and `{71, 74}`;
- IVE: `{63, 62, 87, 88}`;
- IVF: `{97, 96}`.

These sets were not reconstructed from numbering patterns or from the `p` and
`s` operations outside the rendered figure.

## 4. Authoritative source transcription

Topology notation uses `--` for series and `||` for parallel composition;
parentheses fix grouping. Component subscripts in the drawings distinguish
primitives but not values, so the normalized expressions below retain element
kinds rather than source subscripts. Every row has four primitive elements.
Locator cells below use `printed page / zero-based PDF index` and list Appendix
D, Figure 6.2, then Table 6.11.

| Canonical network | Elements | Inventory | Subfamily | Source class | Exact source orbit | Explicit coloured topology | Exact source locators (Appendix D; Figure 6.2; Table 6.11) |
|---:|---:|---|---|---|---|---|---|
| 20 | 4 | R2 C2 | IVA | `IV_A^4` | `{35,28,43,20}` | `R -- C -- (R || C)` | 138/144; 50/56; 58/64 |
| 21 | 4 | R2 C2 | IVA | `IV_A^4` | `{36,29,44,21}` | `R -- (C || (R -- C))` | 138/144; 50/56; 58/64 |
| 22 | 4 | R2 C2 | IVA | `IV_A^4` | `{37,30,45,22}` | `C -- (R || (R -- C))` | 138/144; 50/56; 58/64 |
| 23 | 4 | R2 C2 | IVB | `IV_B^4` | `{38,31,46,23}` | `(R -- C) || (R -- C)` | 139/145; 50/56; 59/65 |
| 24 | 4 | R2 L1 C1 | IVC | `IV_C^4` | `{40,33,48,24}` | `C -- (R || (R -- L))` | 139/145; 50/56; 59/65 |
| 25 | 4 | R2 L1 C1 | IVC | `IV_C^4` | `{39,32,47,25}` | `R -- C -- (R || L)` | 139/145; 50/56; 59/65 |
| 28 | 4 | R2 L2 | IVA | `IV_A^2` | `{35,28,43,20}` | `R -- L -- (R || L)` | 138/144; 50/56; 58/64 |
| 29 | 4 | R2 L2 | IVA | `IV_A^2` | `{36,29,44,21}` | `R -- (L || (R -- L))` | 138/144; 50/56; 58/64 |
| 30 | 4 | R2 L2 | IVA | `IV_A^2` | `{37,30,45,22}` | `L -- (R || (R -- L))` | 138/144; 50/56; 58/64 |
| 31 | 4 | R2 L2 | IVB | `IV_B^2` | `{38,31,46,23}` | `(R -- L) || (R -- L)` | 139/145; 50/56; 59/65 |
| 32 | 4 | R2 L1 C1 | IVC | `IV_C^2` | `{39,32,47,25}` | `R -- L -- (R || C)` | 139/145; 50/56; 59/65 |
| 33 | 4 | R2 L1 C1 | IVC | `IV_C^2` | `{40,33,48,24}` | `L -- (R || (R -- C))` | 139/145; 50/56; 59/65 |
| 35 | 4 | R2 L2 | IVA | `IV_A^1` | `{35,28,43,20}` | `R || (R -- L) || L` | 138/144; 50/56; 58/64 |
| 36 | 4 | R2 L2 | IVA | `IV_A^1` | `{36,29,44,21}` | `R || (L -- (R || L))` | 138/144; 50/56; 58/64 |
| 37 | 4 | R2 L2 | IVA | `IV_A^1` | `{37,30,45,22}` | `L || (R -- (R || L))` | 138/144; 50/56; 58/64 |
| 38 | 4 | R2 L2 | IVB | `IV_B^1` | `{38,31,46,23}` | `(R || L) -- (R || L)` | 139/145; 50/56; 59/65 |
| 39 | 4 | R2 L1 C1 | IVC | `IV_C^1` | `{39,32,47,25}` | `R || (R -- C) || L` | 139/145; 50/56; 59/65 |
| 40 | 4 | R2 L1 C1 | IVC | `IV_C^1` | `{40,33,48,24}` | `L || (R -- (R || C))` | 139/145; 50/56; 59/65 |
| 43 | 4 | R2 C2 | IVA | `IV_A^3` | `{35,28,43,20}` | `R || (R -- C) || C` | 138/144; 50/56; 58/64 |
| 44 | 4 | R2 C2 | IVA | `IV_A^3` | `{36,29,44,21}` | `R || (C -- (R || C))` | 138/144; 50/56; 58/64 |
| 45 | 4 | R2 C2 | IVA | `IV_A^3` | `{37,30,45,22}` | `C || (R -- (R || C))` | 138/144; 50/56; 58/64 |
| 46 | 4 | R2 C2 | IVB | `IV_B^3` | `{38,31,46,23}` | `(R || C) -- (R || C)` | 139/145; 50/56; 59/65 |
| 47 | 4 | R2 L1 C1 | IVC | `IV_C^3` | `{39,32,47,25}` | `R || (R -- L) || C` | 139/145; 50/56; 59/65 |
| 48 | 4 | R2 L1 C1 | IVC | `IV_C^3` | `{40,33,48,24}` | `C || (R -- (R || L))` | 139/145; 50/56; 59/65 |
| 62 | 4 | R2 L1 C1 | IVE | `IV_E^2` | `{63,62,87,88}` | `R || (L -- (R || C))` | 140/146; 50/56; 59/65 |
| 63 | 4 | R2 L1 C1 | IVE | `IV_E^1` | `{63,62,87,88}` | `R -- (L || (R -- C))` | 140/146; 50/56; 59/65 |
| 71 | 4 | R2 L1 C1 | IVD | `IV_D^1` | `{71,74}` | `R -- (R || (L -- C))` | 140/146; 50/56; 59/65 |
| 72 | 4 | R2 L1 C1 | IVD | `IV_D^1` | `{72,73}` | `R || (R -- L -- C)` | 140/146; 50/56; 59/65 |
| 73 | 4 | R2 L1 C1 | IVD | `IV_D^2` | `{72,73}` | `R -- (R || L || C)` | 140/146; 50/56; 59/65 |
| 74 | 4 | R2 L1 C1 | IVD | `IV_D^2` | `{71,74}` | `R || (R -- (L || C))` | 140/146; 50/56; 59/65 |
| 87 | 4 | R2 L1 C1 | IVE | `IV_E^3` | `{63,62,87,88}` | `R -- (C || (R -- L))` | 140/146; 50/56; 59/65 |
| 88 | 4 | R2 L1 C1 | IVE | `IV_E^4` | `{63,62,87,88}` | `R || (C -- (R || L))` | 140/146; 50/56; 59/65 |
| 96 | 4 | R2 L1 C1 | IVF | `IV_F^2` | `{97,96}` | `(R || C) -- (R || L)` | 140/146; 50/56; 59/65 |
| 97 | 4 | R2 L1 C1 | IVF | `IV_F^1` | `{97,96}` | `(R -- C) || (R -- L)` | 140/146; 50/56; 59/65 |

The class allocations agree exactly with the 20 Table 6.11 rows. In
particular, the rendered network 73 has three parallel `R`, `L`, and `C`
branches after its leading resistor; it is not inferred from the visually
similar network 32.

## 5. Independently derived RICE matches

Every topology in Section 4 was separately encoded as a coloured
`PrimitiveNetwork` with terminals `A` and `Z`. All 148 catalogue rows were
indexed with `network_from_descriptor` and
`canonical_structural_signature`. Matching used exactly
`colour-preserving-port-augmented-cycle-matroid-v1`; no descriptor string,
number order, orbit, class, duality, frequency inversion, transformation arrow,
or earlier reduction target was a matching predicate.

The representative descriptor is the catalogue's immutable representative of
the same structural class. For source drawings whose direct graph descriptor
has a different order along a series arm, agreement is exact under the named
cycle-matroid relation, which includes series interchange; it is not asserted
as descriptor-text equality.

| Canonical network | Fixture ID | Unique RICE catalogue ID | Representative descriptor | Inventory | Relation | Cardinality | Current disposition | Evidence locator |
|---:|---|---|---|---|---|---:|---|---|
| 20 | `ms-c108-four-20` | `lh148-e4990ea5b5b75ace` | `0-2:C;0-2:R;1-3:C;2-3:R` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 21 | `ms-c108-four-21` | `lh148-79cf9dd24646a1a1` | `0-2:C;0-3:C;1-2:R;2-3:R` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 22 | `ms-c108-four-22` | `lh148-53e805bd81449a69` | `0-2:C;0-3:R;1-3:C;2-3:R` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 23 | `ms-c108-four-23` | `lh148-40b10a9f485445a8` | `0-2:C;0-3:C;1-2:R;1-3:R` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 24 | `ms-c108-four-24` | `lh148-0f581053d03369e2` | `0-2:C;1-2:R;1-3:L;2-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 25 | `ms-c108-four-25` | `lh148-2fe78de797e54618` | `0-2:C;1-3:L;1-3:R;2-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 28 | `ms-c108-four-28` | `lh148-354f03447076bf4a` | `0-2:L;0-2:R;1-3:L;2-3:R` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 29 | `ms-c108-four-29` | `lh148-867793e6aaaea530` | `0-2:L;0-3:L;1-2:R;2-3:R` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 30 | `ms-c108-four-30` | `lh148-366759d751e644ba` | `0-2:L;0-3:R;1-3:L;2-3:R` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 31 | `ms-c108-four-31` | `lh148-0b27d33003f81032` | `0-2:L;0-3:L;1-2:R;1-3:R` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 32 | `ms-c108-four-32` | `lh148-c4a008c923682500` | `0-2:C;0-2:R;1-3:L;2-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 33 | `ms-c108-four-33` | `lh148-4d6ac6885b8efb8e` | `0-2:C;0-3:R;1-3:L;2-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 35 | `ms-c108-four-35` | `lh148-a1a63778c0bb98e8` | `0-1:L;0-1:R;0-2:L;1-2:R` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 36 | `ms-c108-four-36` | `lh148-af3808b69e5fc54f` | `0-1:R;0-2:L;0-2:R;1-2:L` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 37 | `ms-c108-four-37` | `lh148-e61bc7a989c01099` | `0-1:L;0-2:L;0-2:R;1-2:R` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 38 | `ms-c108-four-38` | `lh148-ff2aaae76070d52a` | `0-2:L;0-2:R;1-2:L;1-2:R` | R2 L2 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 39 | `ms-c108-four-39` | `lh148-05ef035064872f96` | `0-1:L;0-1:R;0-2:C;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 40 | `ms-c108-four-40` | `lh148-cdfcaba8001db4d0` | `0-1:L;0-2:C;0-2:R;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 43 | `ms-c108-four-43` | `lh148-02b69ac8bc305a1f` | `0-1:C;0-1:R;0-2:C;1-2:R` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 44 | `ms-c108-four-44` | `lh148-fad884ca638a4191` | `0-1:R;0-2:C;0-2:R;1-2:C` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 45 | `ms-c108-four-45` | `lh148-102b49d775bd5eb8` | `0-1:C;0-2:C;0-2:R;1-2:R` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 138 / index 144; reproduction below |
| 46 | `ms-c108-four-46` | `lh148-c89875389584ae09` | `0-2:C;0-2:R;1-2:C;1-2:R` | R2 C2 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 47 | `ms-c108-four-47` | `lh148-343285fa13b9f794` | `0-1:C;0-1:R;0-2:L;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 48 | `ms-c108-four-48` | `lh148-5a15c54aa65b57dc` | `0-1:C;0-2:L;0-2:R;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 139 / index 145; reproduction below |
| 62 | `ms-c108-four-62` | `lh148-b9495748ed67c6d6` | `0-1:R;0-2:C;0-2:R;1-2:L` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 63 | `ms-c108-four-63` | `lh148-47aef84ec8f4741c` | `0-2:C;0-3:L;1-3:R;2-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 71 | `ms-c108-four-71` | `lh148-4fef33c7e96b6566` | `0-2:C;0-3:R;1-3:R;2-3:L` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 72 | `ms-c108-four-72` | `lh148-67980e5858742b26` | `0-1:R;0-2:C;1-3:L;2-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 73 | `ms-c108-four-73` | `lh148-21e4f9e2ce897b40` | `0-2:C;0-2:L;0-2:R;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 74 | `ms-c108-four-74` | `lh148-3419842c4cffff68` | `0-1:R;0-2:C;0-2:L;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 87 | `ms-c108-four-87` | `lh148-68712beedefbc0fa` | `0-2:C;0-3:L;1-2:R;2-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 88 | `ms-c108-four-88` | `lh148-8a1860e27fc40c7f` | `0-1:R;0-2:C;1-2:L;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 96 | `ms-c108-four-96` | `lh148-5cb1f71c6efaef26` | `0-2:C;0-2:R;1-2:L;1-2:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |
| 97 | `ms-c108-four-97` | `lh148-74be9e435c3d69b8` | `0-2:C;0-3:L;1-2:R;1-3:R` | R2 L1 C1 | named relation | 1 | unresolved | Appendix D p. 140 / index 146; reproduction below |

“Named relation” in the compact table means exactly
`colour-preserving-port-augmented-cycle-matroid-v1`.

## 6. Census result and reduction-target boundary

Every fixture has exactly one matching RICE row. The 34 rows are distinct,
have four elements and the source-drawn inventories, and are all currently
`unresolved`; none is among the forty exclusions or 25 retained low-order
rows. They exhaust the ledger's unresolved four-element population. The other
49 unresolved rows all have five elements.

Earlier evidence records use several of these canonical numbers as reduction
or conditional simpler-realisation destinations. The reproduction audit reads
all historical identifiers and confirms that none of the 34 identities was
obtained from such a target: the mapping dictionary is built only from each
rendered fixture's structural signature. A five-element subject reducing to
canonical network 72, for example, does not identify that excluded subject as
network 72 and did not supply `lh148-67980e5858742b26`.

## 7. Equivalence and orbit boundary

The class and orbit columns are authoritative source transcriptions. The RICE
calculation establishes only coloured two-terminal structural identity between
each rendered fixture and one catalogue row. It does not independently
reproduce the 20 realizability-set classes, the ten source orbits, or the
complete 62-class behavioural classification. A dashed Zobel link may record a
source equivalence without becoming a general RICE transformation contract.

## 8. Previous-workspace audit

This bounded audit was performed only after the PDF transcription and RICE
matching were complete. The sibling repositories were read-only and clean at:

- `../network-theory` commit
  `87b831831c154c5c3675853a99ff7e5a2b7dfb6d`;
- `../pynntt` commit `f3db06032cbe23d583d77f6cb79d21ced90d7651`;
- `../pynntt_lab` commit `1ddd90034da4594bb6a3728b0700918883fd1172`.

The `network-theory` directory
`016--graph-generation/doc/ladenheim-catalogue/ladenheim-schematics/`
contains numbered PNGs for the four-element source numbers. A bounded visual
sample of networks 20, 37, 73, and 97 agrees with the independent Appendix D
transcription, including the three parallel reactive/resistive branches in
network 73. No relevant numbered mapping was found in the bounded `pynntt` or
`pynntt_lab` text search. No sibling record supplied a topology, number, class,
orbit, or RICE ID used in this report.

## 9. Conclusions and limitations

The authoritative four-element inventory is 34 networks in six subfamilies,
20 equivalence classes, and ten orbits. The independently transcribed fixtures
select exactly 34 distinct RICE subjects, one per source diagram, and exhaust
the current unresolved four-element population.

This report provides evidence for a later identity-contract and application
milestone. It does not populate the 34 historical identifiers or retained
dispositions, claim that the full canonical 108 has been reproduced, or begin
the 108-to-62 classification. The publication prints canonical diagrams and
numbers, not `lh148-*` catalogue IDs; each RICE correspondence above is an
independently reproduced conclusion.

## 10. Reproduction commands

Run this paste-ready block from the RICE repository root. It uses only existing
RICE APIs and the Python standard library, scans all 148 catalogue rows, and
fails on a missing, duplicate, excluded, retained, or non-unique match.

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


def S(*parts):
    return ("S", *parts)


def P(*parts):
    return ("P", *parts)


def fixture(expression):
    edges = []
    counter = [0]

    def fresh():
        counter[0] += 1
        return f"n{counter[0]}"

    def emit(part, left, right):
        if isinstance(part, str):
            edges.append(PrimitiveEdge(left, right, part))
            return
        operation, *children = part
        if operation == "P":
            for child in children:
                emit(child, left, right)
            return
        assert operation == "S"
        nodes = [left] + [fresh() for _ in children[:-1]] + [right]
        for child, u, v in zip(children, nodes, nodes[1:]):
            emit(child, u, v)

    emit(expression, "A", "Z")
    return PrimitiveNetwork(("A", "Z"), tuple(edges))


expressions = {
    20: S("R", "C", P("R", "C")),
    21: S("R", P("C", S("R", "C"))),
    22: S("C", P("R", S("R", "C"))),
    23: P(S("R", "C"), S("R", "C")),
    24: S("C", P("R", S("R", "L"))),
    25: S("R", "C", P("R", "L")),
    28: S("R", "L", P("R", "L")),
    29: S("R", P("L", S("R", "L"))),
    30: S("L", P("R", S("R", "L"))),
    31: P(S("R", "L"), S("R", "L")),
    32: S("R", "L", P("R", "C")),
    33: S("L", P("R", S("R", "C"))),
    35: P("R", S("R", "L"), "L"),
    36: P("R", S("L", P("R", "L"))),
    37: P("L", S("R", P("R", "L"))),
    38: S(P("R", "L"), P("R", "L")),
    39: P("R", S("R", "C"), "L"),
    40: P("L", S("R", P("R", "C"))),
    43: P("R", S("R", "C"), "C"),
    44: P("R", S("C", P("R", "C"))),
    45: P("C", S("R", P("R", "C"))),
    46: S(P("R", "C"), P("R", "C")),
    47: P("R", S("R", "L"), "C"),
    48: P("C", S("R", P("R", "L"))),
    62: P("R", S("L", P("R", "C"))),
    63: S("R", P("L", S("R", "C"))),
    71: S("R", P("R", S("L", "C"))),
    72: P("R", S("R", "L", "C")),
    73: S("R", P("R", "L", "C")),
    74: P("R", S("R", P("L", "C"))),
    87: S("R", P("C", S("R", "L"))),
    88: P("R", S("C", P("R", "L"))),
    96: S(P("R", "C"), P("R", "L")),
    97: P(S("R", "C"), S("R", "L")),
}

metadata = {
    20: ("IVA", "IV_A^4", (2, 0, 2), (35, 28, 43, 20)),
    21: ("IVA", "IV_A^4", (2, 0, 2), (36, 29, 44, 21)),
    22: ("IVA", "IV_A^4", (2, 0, 2), (37, 30, 45, 22)),
    23: ("IVB", "IV_B^4", (2, 0, 2), (38, 31, 46, 23)),
    24: ("IVC", "IV_C^4", (2, 1, 1), (40, 33, 48, 24)),
    25: ("IVC", "IV_C^4", (2, 1, 1), (39, 32, 47, 25)),
    28: ("IVA", "IV_A^2", (2, 2, 0), (35, 28, 43, 20)),
    29: ("IVA", "IV_A^2", (2, 2, 0), (36, 29, 44, 21)),
    30: ("IVA", "IV_A^2", (2, 2, 0), (37, 30, 45, 22)),
    31: ("IVB", "IV_B^2", (2, 2, 0), (38, 31, 46, 23)),
    32: ("IVC", "IV_C^2", (2, 1, 1), (39, 32, 47, 25)),
    33: ("IVC", "IV_C^2", (2, 1, 1), (40, 33, 48, 24)),
    35: ("IVA", "IV_A^1", (2, 2, 0), (35, 28, 43, 20)),
    36: ("IVA", "IV_A^1", (2, 2, 0), (36, 29, 44, 21)),
    37: ("IVA", "IV_A^1", (2, 2, 0), (37, 30, 45, 22)),
    38: ("IVB", "IV_B^1", (2, 2, 0), (38, 31, 46, 23)),
    39: ("IVC", "IV_C^1", (2, 1, 1), (39, 32, 47, 25)),
    40: ("IVC", "IV_C^1", (2, 1, 1), (40, 33, 48, 24)),
    43: ("IVA", "IV_A^3", (2, 0, 2), (35, 28, 43, 20)),
    44: ("IVA", "IV_A^3", (2, 0, 2), (36, 29, 44, 21)),
    45: ("IVA", "IV_A^3", (2, 0, 2), (37, 30, 45, 22)),
    46: ("IVB", "IV_B^3", (2, 0, 2), (38, 31, 46, 23)),
    47: ("IVC", "IV_C^3", (2, 1, 1), (39, 32, 47, 25)),
    48: ("IVC", "IV_C^3", (2, 1, 1), (40, 33, 48, 24)),
    62: ("IVE", "IV_E^2", (2, 1, 1), (63, 62, 87, 88)),
    63: ("IVE", "IV_E^1", (2, 1, 1), (63, 62, 87, 88)),
    71: ("IVD", "IV_D^1", (2, 1, 1), (71, 74)),
    72: ("IVD", "IV_D^1", (2, 1, 1), (72, 73)),
    73: ("IVD", "IV_D^2", (2, 1, 1), (72, 73)),
    74: ("IVD", "IV_D^2", (2, 1, 1), (71, 74)),
    87: ("IVE", "IV_E^3", (2, 1, 1), (63, 62, 87, 88)),
    88: ("IVE", "IV_E^4", (2, 1, 1), (63, 62, 87, 88)),
    96: ("IVF", "IV_F^2", (2, 1, 1), (97, 96)),
    97: ("IVF", "IV_F^1", (2, 1, 1), (97, 96)),
}

expected_subfamilies = {
    "IVA": (12, 4, 3),
    "IVB": (4, 4, 1),
    "IVC": (8, 4, 2),
    "IVD": (4, 2, 2),
    "IVE": (4, 4, 1),
    "IVF": (2, 2, 1),
}

catalogue = json.loads(Path("data/counts/ladenheim-148.json").read_text())
ledger = json.loads(
    Path("data/comparisons/ladenheim-148-to-108.json").read_text()
)
assert len(catalogue["records"]) == 148
assert ledger["summary"]["by_proposed_disposition"] == {
    "exclude": 40,
    "retain": 25,
    "unresolved": 83,
}
assert all(row["basic_graph_assignment"] is None for row in ledger["records"])
identifier_rows = [row for row in ledger["records"] if row["historical_identifiers"]]
assert len(identifier_rows) == 25
assert all(len(row["historical_identifiers"]) == 1 for row in identifier_rows)
assert all(
    row["historical_identifiers"][0]["scheme"]
    == "morelli-smith-canonical-network"
    for row in identifier_rows
)

ledger_rows = {row["catalogue_id"]: row for row in ledger["records"]}
catalogue_by_signature = {}
for row in catalogue["records"]:
    signature = canonical_structural_signature(
        network_from_descriptor(row["representative_descriptor"])
    )
    assert signature.relation == RELATION
    catalogue_by_signature.setdefault(signature, []).append(row)

matches = {}
for number in sorted(expressions):
    source_fixture = fixture(expressions[number])
    signature = canonical_structural_signature(source_fixture)
    assert signature.relation == RELATION
    rows = catalogue_by_signature.get(signature, [])
    assert len(rows) == 1, (number, [row["catalogue_id"] for row in rows])
    row = rows[0]
    subfamily, eq_class, inventory, orbit = metadata[number]
    assert source_fixture.counts == inventory
    assert (row["r"], row["l"], row["c"]) == inventory
    assert row["rlc"] == 4
    production_row = ledger_rows[row["catalogue_id"]]
    assert production_row["comparison_status"] == "unresolved"
    assert production_row["proposed_disposition"] == "unresolved"
    assert production_row["historical_identifiers"] == []
    matches[number] = row
    print(
        f"network {number:>2} {subfamily} {eq_class} -> "
        f"{row['catalogue_id']} {row['representative_descriptor']}"
    )

assert set(matches) == {
    20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33,
    35, 36, 37, 38, 39, 40, 43, 44, 45, 46, 47, 48,
    62, 63, 71, 72, 73, 74, 87, 88, 96, 97,
}
assert len({row["catalogue_id"] for row in matches.values()}) == 34
assert len({f"ms-c108-four-{number}" for number in matches}) == 34

for subfamily, (network_count, class_count, orbit_count) in (
    expected_subfamilies.items()
):
    numbers = [n for n, value in metadata.items() if value[0] == subfamily]
    assert len(numbers) == network_count
    assert len({metadata[n][1] for n in numbers}) == class_count
    assert len({metadata[n][3] for n in numbers}) == orbit_count
assert sum(value[0] for value in expected_subfamilies.values()) == 34
assert sum(value[1] for value in expected_subfamilies.values()) == 20
assert sum(value[2] for value in expected_subfamilies.values()) == 10

unresolved = [
    row for row in ledger["records"]
    if row["proposed_disposition"] == "unresolved"
]
unresolved_four = {row["catalogue_id"] for row in unresolved if row["rlc"] == 4}
unresolved_five = {row["catalogue_id"] for row in unresolved if row["rlc"] == 5}
assert unresolved_four == {row["catalogue_id"] for row in matches.values()}
assert len(unresolved_five) == 49
assert len(unresolved_four | unresolved_five) == 83

# Reduction destinations are not identities. Only the retained low-order rows
# carry canonical historical identifiers, and none of the 34 matches does.
assert not any(
    ledger_rows[row["catalogue_id"]]["historical_identifiers"]
    for row in matches.values()
)

print("source inventory: 34 networks; 6 subfamilies; 20 classes; 10 orbits")
print("structural matches: 34 distinct unique unresolved RICE subjects")
print("unresolved census: 34 four-element + 49 five-element = 83")
print("production unchanged: 40 excluded / 83 unresolved / 25 retained")
print("identifiers: 25 populated low-order rows; graph assignments: 148 null")
PY
```

## 11. Observed reproduction output

The output below was recorded after executing the exact block above.

```text
network 20 IVA IV_A^4 -> lh148-e4990ea5b5b75ace 0-2:C;0-2:R;1-3:C;2-3:R
network 21 IVA IV_A^4 -> lh148-79cf9dd24646a1a1 0-2:C;0-3:C;1-2:R;2-3:R
network 22 IVA IV_A^4 -> lh148-53e805bd81449a69 0-2:C;0-3:R;1-3:C;2-3:R
network 23 IVB IV_B^4 -> lh148-40b10a9f485445a8 0-2:C;0-3:C;1-2:R;1-3:R
network 24 IVC IV_C^4 -> lh148-0f581053d03369e2 0-2:C;1-2:R;1-3:L;2-3:R
network 25 IVC IV_C^4 -> lh148-2fe78de797e54618 0-2:C;1-3:L;1-3:R;2-3:R
network 28 IVA IV_A^2 -> lh148-354f03447076bf4a 0-2:L;0-2:R;1-3:L;2-3:R
network 29 IVA IV_A^2 -> lh148-867793e6aaaea530 0-2:L;0-3:L;1-2:R;2-3:R
network 30 IVA IV_A^2 -> lh148-366759d751e644ba 0-2:L;0-3:R;1-3:L;2-3:R
network 31 IVB IV_B^2 -> lh148-0b27d33003f81032 0-2:L;0-3:L;1-2:R;1-3:R
network 32 IVC IV_C^2 -> lh148-c4a008c923682500 0-2:C;0-2:R;1-3:L;2-3:R
network 33 IVC IV_C^2 -> lh148-4d6ac6885b8efb8e 0-2:C;0-3:R;1-3:L;2-3:R
network 35 IVA IV_A^1 -> lh148-a1a63778c0bb98e8 0-1:L;0-1:R;0-2:L;1-2:R
network 36 IVA IV_A^1 -> lh148-af3808b69e5fc54f 0-1:R;0-2:L;0-2:R;1-2:L
network 37 IVA IV_A^1 -> lh148-e61bc7a989c01099 0-1:L;0-2:L;0-2:R;1-2:R
network 38 IVB IV_B^1 -> lh148-ff2aaae76070d52a 0-2:L;0-2:R;1-2:L;1-2:R
network 39 IVC IV_C^1 -> lh148-05ef035064872f96 0-1:L;0-1:R;0-2:C;1-2:R
network 40 IVC IV_C^1 -> lh148-cdfcaba8001db4d0 0-1:L;0-2:C;0-2:R;1-2:R
network 43 IVA IV_A^3 -> lh148-02b69ac8bc305a1f 0-1:C;0-1:R;0-2:C;1-2:R
network 44 IVA IV_A^3 -> lh148-fad884ca638a4191 0-1:R;0-2:C;0-2:R;1-2:C
network 45 IVA IV_A^3 -> lh148-102b49d775bd5eb8 0-1:C;0-2:C;0-2:R;1-2:R
network 46 IVB IV_B^3 -> lh148-c89875389584ae09 0-2:C;0-2:R;1-2:C;1-2:R
network 47 IVC IV_C^3 -> lh148-343285fa13b9f794 0-1:C;0-1:R;0-2:L;1-2:R
network 48 IVC IV_C^3 -> lh148-5a15c54aa65b57dc 0-1:C;0-2:L;0-2:R;1-2:R
network 62 IVE IV_E^2 -> lh148-b9495748ed67c6d6 0-1:R;0-2:C;0-2:R;1-2:L
network 63 IVE IV_E^1 -> lh148-47aef84ec8f4741c 0-2:C;0-3:L;1-3:R;2-3:R
network 71 IVD IV_D^1 -> lh148-4fef33c7e96b6566 0-2:C;0-3:R;1-3:R;2-3:L
network 72 IVD IV_D^1 -> lh148-67980e5858742b26 0-1:R;0-2:C;1-3:L;2-3:R
network 73 IVD IV_D^2 -> lh148-21e4f9e2ce897b40 0-2:C;0-2:L;0-2:R;1-2:R
network 74 IVD IV_D^2 -> lh148-3419842c4cffff68 0-1:R;0-2:C;0-2:L;1-2:R
network 87 IVE IV_E^3 -> lh148-68712beedefbc0fa 0-2:C;0-3:L;1-2:R;2-3:R
network 88 IVE IV_E^4 -> lh148-8a1860e27fc40c7f 0-1:R;0-2:C;1-2:L;1-2:R
network 96 IVF IV_F^2 -> lh148-5cb1f71c6efaef26 0-2:C;0-2:R;1-2:L;1-2:R
network 97 IVF IV_F^1 -> lh148-74be9e435c3d69b8 0-2:C;0-3:L;1-2:R;1-3:R
source inventory: 34 networks; 6 subfamilies; 20 classes; 10 orbits
structural matches: 34 distinct unique unresolved RICE subjects
unresolved census: 34 four-element + 49 five-element = 83
production unchanged: 40 excluded / 83 unresolved / 25 retained
identifiers: 25 populated low-order rows; graph assignments: 148 null
```
