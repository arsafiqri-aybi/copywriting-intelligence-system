# Knowledge Retrieval

Use this reference for nontrivial strategy, critique, research-grounded explanation, or experiment design.

## Start with seeds

Seed retrieval from:

- S5 mapping target nodes;
- explicit belief/trust/friction problems;
- required message-design decisions.

## Graph policy

Read `reasoning/retrieval-policy.json`.

Default:

- accepted nodes first;
- accepted one-hop edges first;
- provisional nodes/edges only when directly material;
- one hop by default;
- two hops only for mediation, conflict, or a decision-critical dependency.

Stop when more retrieval no longer changes a material strategy decision, uncertainty, conflict, or experiment candidate.

## Registries

- `research/registry/nodes.json` — canonical/provisional constructs.
- `research/registry/edges.json` — evidence-backed/provisional cross-core relationships.
- `research/registry/claims.json` — atomic scientific claims and provenance.
- `research/registry/contradictions.json` — null/mixed/contradictory evidence.
- `research/registry/uncertainties.json` — unresolved uncertainty and transport limits.
- `research/registry/measurements.json` — construct measurement mappings.

Do not load the entire research library for a simple rewrite.
