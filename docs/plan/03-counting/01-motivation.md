# 03-counting / 01 — Explain enumeration motivation

Status: `todo`

## Goal

Explain why enumerating small RLC networks matters for Pynntt and for network theory.

## Draft motivation

Enumerating finite classes of RLC one-port networks is useful because it turns vague questions about possible circuit forms into reproducible catalogues. A catalogue can be searched, counted, compared with known results, and used to test hypotheses about realisability and minimality.

For Pynntt specifically, enumeration can help to:

- test whether the descriptor language covers the intended classes of networks;
- discover duplicate descriptors that describe equivalent networks;
- build canonicalisation rules from evidence rather than guesswork;
- generate golden examples for impedance calculation and simplification tests;
- compare Pynntt output with historical catalogues;
- explore where series-parallel forms cease to be enough and bridge-like primitives become necessary;
- support future claims about completeness, expressiveness, and minimal realisations.

## Done means

- The repository contains a clear motivation note.
- The note distinguishes practical software motivation from mathematical claims.
- Any historical catalogue comparisons are cited in the documentation.
