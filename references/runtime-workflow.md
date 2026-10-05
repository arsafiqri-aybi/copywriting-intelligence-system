# Deep Runtime Workflow

Use for strategy-heavy work, diagnosis, audit, or when the copy request has conflicting constraints/evidence.

1. Ground the commercial context using S5.
2. Resolve signals with `market_value/mapping-rules.json`.
3. Retrieve the smallest relevant node/edge subgraph.
4. Build an activation ledger: primary, supporting, countervailing, constraint, uncertainty.
5. Detect active conflicts with `reasoning/conflict-catalog.json`.
6. Propagate uncertainty with `reasoning/uncertainty-policy.json`.
7. Select operational actions from `reasoning/strategy-rules.json`; treat them as runtime design rules, not effect-size claims.
8. Build an evidence-locked generation packet using `schemas/generation-packet.schema.json`.
9. Generate copy under the fact/claim lock.
10. Critique using `reasoning/critique-protocol.json`.
11. For uncertain material decisions, emit an experiment hook rather than fake certainty.
12. If performance data exists, apply S7 feedback rules.

Do not expose the full internal activation ledger by default. Give the user the level of explanation they requested.
