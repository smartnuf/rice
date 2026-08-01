# 00-records / 03 — Update README motivation for enumeration

Status: `done`

## Goal

Plan and maintain a README motivation note explaining why enumerating small RLC networks matters for rice and for network theory.

## Draft motivation

Enumerating finite classes of RLC one-port networks is useful because it turns vague questions about possible circuit forms into reproducible catalogues. A catalogue can be searched, counted, compared with known results, and used to test hypotheses about realisability and minimality.

For rice specifically, enumeration can help to:

- test whether the descriptor language covers the intended classes of networks;
- discover duplicate descriptors that describe equivalent networks;
- build canonicalisation rules from evidence rather than guesswork;
- generate golden examples for impedance calculation and simplification tests;
- compare rice output with historical catalogues;
- explore where series-parallel forms cease to be enough and bridge-like primitives become necessary;
- support future claims about completeness, expressiveness, and minimal realisations.

## Done means

- The README has a concise motivation section useful to a new reader.
- The note distinguishes practical software motivation from mathematical claims.
- Detailed historical catalogue comparisons and citations remain tracked
  separately in [`08-docs/03-catalogues.md`](../08-docs/03-catalogues.md).


## Progress notes

- `README.md` now explains how reproducible catalogues support object and
  descriptor coverage, duplicate detection, canonicalisation, golden cases,
  named-contract comparisons, SP/bridge investigation, and later mathematical
  work.
- The section distinguishes current reproducible software capabilities from
  unproved completeness, minimality, realisability, and historical-agreement
  claims. Completing the separate historical comparison and citation task is
  not a blocker for this general motivation record.
