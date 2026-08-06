# Roadmap Progress Update

#### You:
Show me where we are on our roadmap / plan at this point.

#### ChatGPT:
## Current checkpoint

We have completed the first major Ladenheim programme:

**148 structural networks → 108 canonical networks**

After [PR #89](https://github.com/smartnuf/rice/pull/89), `main` records:

- **40 excluded**
- **108 retained**
- **0 unresolved**
- all retained subjects mapped uniquely to canonical numbers **1-108**
- all 148 structural subjects accounted for
- basic-graph-letter assignments deliberately still unset
- full test suite: **769 passed**

There are currently **no open RICE pull requests**. The latest commit on `main` is the merge of PR #89.

The plan index now explicitly identifies the completed 148 and 108 milestones and names independent reproduction of the 62 behavioural classes as the next Ladenheim milestone.

## Roadmap position

| Workstream                                     | Position                                    |
| ---------------------------------------------- | ------------------------------------------- |
| Development environment                        | **Done**                                    |
| Old implementation cleanup                     | **Done**                                    |
| Object-oriented counting language              | **Done**                                    |
| Small and Ladenheim enumeration slices         | **Done**                                    |
| Structural Ladenheim 148                       | **Done**                                    |
| Forty historical exclusions                    | **Done**                                    |
| Canonical Ladenheim 108 identities             | **Done**                                    |
| Canonical numbering 1-108                      | **Done**                                    |
| 62 realizability-set classes                   | **Next substantive milestone**              |
| Generator sets                                 | After or alongside the 62-class work        |
| SP/bridge descriptor integration               | Still todo                                  |
| Comparison of reduction/equivalence contracts  | Still todo                                  |
| Larger enumeration slices                      | Later                                       |
| General biquadratic sufficiency investigations | Later, dependent on the catalogue machinery |
| Tests, methodology and documentation           | Ongoing cross-cutting work                  |

The plan is organized by subject and dependency rather than as a strict chronological queue, so the remaining `prog` items in counting, testing and documentation are continuing maintenance tracks rather than prerequisites that must all be closed first.

## What changes at the next milestone

The next task is **not another structural matching exercise**.

The source’s 62 classes concern **realisability-set equivalence**: networks belong together because they realise the same class of impedance functions, not merely because their graphs, coloured structures, or reduction histories match.

The recorded task therefore requires us to:

- derive the 62 classes from the 108 networks using documented behavioural criteria;
- keep them separate from graph 2-isomorphism, local series/parallel reduction and star-delta processing;
- keep the 62 classes distinct from the reported **35 group-action orbits** and **24 subfamilies**.

This distinction is important because the repository now contains several different relations that could otherwise be conflated:

```text
structural identity
    ≠ orbit membership
    ≠ source subfamily
    ≠ local SP reduction
    ≠ Y-Δ / star-delta relation
    ≠ Zobel transformation
    ≠ simpler-realisation containment
    ≠ realisability-set equivalence
```

## Likely sequence from here

### Immediate

**1. Establish the evidence and data contract for the 62-class reproduction.**

Before changing production data, determine exactly what evidence proves that two canonical networks have the same realisability set. This should follow the successful evidence-first pattern used for the 148-to-108 work.

**2. Reproduce the classes independently.**

Use the canonical 108 identities as the stable subject population, transcribe the source class claims, and independently establish the class membership criterion for RICE.

**3. Apply the completed classification atomically.**

Once the evidence group is complete and reviewed, expose the 62 classes in generated data and user-facing outputs.

### Following that

**4. Generator sets.**

This is intentionally separate: generator claims may be structural, electrical or behavioural, and must not be confused with the 148, 108 or 62 counts.

**5. Descriptor and reduction integration.**

Bring together SP/bridge descriptors, basic-graph names, canonical numbering and the various named reduction/equivalence relations.

**6. Move outward to larger slices and the biquadratic questions.**

The intended larger census is still `R <= 3`, `L+C <= 5`; the more ambitious sufficiency and sharp-bound investigations remain downstream of reliable enumeration, classification and output machinery.

## Documentation position

The central Ladenheim identity documentation is now substantially complete, but the broader documentation workstream remains `prog`: basic-graph descriptors, wider terminology and the 62-class explanation are still missing.

I also do **not** see a dedicated plan record yet for the accessibility/intelligibility catch-up we discussed-glossary coverage, explaining terms such as orbits and rigid cores, reviewer expectations for readability, and ongoing documentation maintenance. The current `08-docs` tasks are broader and do not fully record that intention.

So the clean current picture is:

> **We have finished reproducing which 108 canonical networks Ladenheim contains.\
> We have not yet independently reproduced why those 108 collapse into 62 behavioural equivalence classes.**

That is the natural point at which to resume.
