# Continuous Research & Invalidation Protocol

## Principle

Release v1.0.0 is stable for use, but scientific saturation is **not claimed**. New evidence enters through a controlled lifecycle and invalidates only affected descendants.

## Intake lifecycle

```text
candidate source
→ screen
→ atomic claim extraction
→ verification
→ contradiction / null / boundary check
→ node or edge promotion decision
→ dependency impact analysis
→ targeted regression
→ versioned release
```

## Invalidation rules

1. **Source metadata correction** — update provenance; rerun only claim references materially affected.
2. **Atomic claim revision** — invalidate dependent node/edge support records and any runtime rule that relies materially on that claim.
3. **Node boundary/status change** — re-audit dependent edges, market mappings, reasoning strategies, measurements, and affected evaluations.
4. **Scientific edge change** — re-audit strategies/conflicts that cite the edge and rerun targeted regression/adversarial cases.
5. **Market mapping change** — rerun S5 mapping cases and affected S6 reasoning cases.
6. **Reasoning/strategy change** — rerun S6 regression and all affected S8 evaluation sets.
7. **Measurement/feedback change** — rerun S7 discipline tests and any evaluation that depends on metric interpretation.
8. **SKILL.md / trigger / runtime reference change** — rerun S9 static, trigger-design, and behavior audits.
9. **Critical finding** — block release promotion until the affected mandatory gate returns to PASS.

## Evidence conflict

Never delete inconvenient null or contradictory results. Record them, compare construct definitions, context, population, operationalization, study design and moderators, then narrow confidence or scope when warranted.

## Versioning

- **PATCH** — wording, metadata, non-behavioral documentation, or bounded bug fix with no architecture change.
- **MINOR** — new accepted/provisional nodes, edges, mappings, strategies, measurements, or evaluation coverage that preserves protected architecture.
- **MAJOR** — protected architecture, runtime contract, or incompatible schema changes.

## Release rule

A new release may be called project/release complete only when every mandatory gate relevant to that release scope is PASS. Research saturation remains a separate claim and defaults to NOT_CLAIMED.
