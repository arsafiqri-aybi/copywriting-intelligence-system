# Evidence Policy

## Core rule

Research is the epistemic substrate of the project.

Use:

```text
SOURCE
→ SOURCE REGISTRY
→ ATOMIC CLAIM
→ VERIFICATION
→ NODE / EDGE SUPPORT
→ REASONING
→ OBSERVATION / EXPERIMENT
→ FEEDBACK
→ CALIBRATED UPDATE
```

## Source/evidence classes

Keep evidence classes distinct. Relevant classes include:

- systematic review / meta-analysis;
- replicated experimental evidence;
- individual randomized/controlled experiment;
- field experiment;
- quasi-experimental evidence;
- longitudinal predictive evidence;
- correlational/observational evidence;
- measurement/validation research;
- mechanistic/theoretical work;
- authoritative standards or regulatory guidance;
- high-quality practitioner evidence;
- anecdotal evidence.

No evidence class automatically dominates every question. Relevance, construct match, population, context, design quality and transportability matter.

## Atomic claims

Scientific statements must be decomposed into atomic claims with explicit stance and provenance.

Supported claim types:

- descriptive;
- association;
- causal;
- mechanistic;
- moderation;
- mediation;
- measurement;
- null;
- contradiction;
- transport/generalization.

A claim may support, contrast, bound or remain neutral toward a node or edge.

## Required claim context when available

Record:

- source;
- study design;
- population;
- sample;
- context;
- operationalization;
- effect estimate;
- uncertainty;
- heterogeneity;
- bias concerns;
- replication information;
- contradictory/null findings;
- boundary conditions;
- generalization/transport limits.

## Scientific edge policy

Do not create edges because two constructs sound related.

Each important edge should preserve:

- source;
- target;
- relation;
- polarity;
- directionality;
- causal status;
- mechanism;
- claim IDs;
- moderators;
- boundary conditions;
- transport limits;
- uncertainty;
- lifecycle status.

An explicit non-edge/rejected relationship is valid research output.

## Effect-size policy

Published effect estimates may be stored with their original scale and context.

Do not automatically:

- normalize unrelated measures into a single pseudo-score;
- treat architecture weights as empirical effect sizes;
- propagate a laboratory effect size as a universal runtime coefficient;
- average contradictory evidence into false certainty.

## Contradictions and null findings

Negative and null findings are first-class evidence.

When evidence conflicts:

1. check construct definitions;
2. compare population/context;
3. compare operationalization;
4. compare study design;
5. inspect moderators and boundary conditions;
6. preserve unresolved disagreement when evidence does not justify resolution.

## Saturation

Research saturation may only be claimed for a defined scope.

Track:

- new construct discovery rate;
- new mechanism discovery;
- new contradiction discovery;
- new boundary-condition discovery;
- new high-quality evidence;
- unresolved critical gaps.

Default state when not demonstrated: `NOT_CLAIMED`.
