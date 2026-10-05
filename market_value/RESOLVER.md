# Market & Value → Mechanism Resolver

## Objective

Convert grounded commercial facts into bounded mechanism hypotheses without treating marketing labels or observed outcomes as latent states.

## Algorithm

### 1. normalize_context
- separate fact from interpretation
- attach provenance
- scope population/channel/time
- mark observed/reported/derived/assumed

### 2. construct_commercial_objects
- build alternative set
- build value hypotheses
- build objection records
- build proof inventory
- build friction map
- retain customer language verbatim

### 3. retrieve_mapping_rules
- match dimension and fact_type
- apply qualifiers
- collect target nodes
- collect non-implications and alternatives

### 4. validate_targets
- target node must exist
- provisional node remains provisional
- scientific edge/claim refs must exist
- no commercial object becomes a node

### 5. aggregate_hypotheses
- combine independent evidence for same node
- preserve contradictory signals
- separate mechanism evidence from strategic convenience

### 6. assign_activation_status
- strong_candidate only when direct/repeated audience evidence matches accepted construct semantics
- candidate when mapping is plausible with adequate but incomplete evidence
- weak_candidate for heuristic/provisional mappings or single ambiguous signals
- do_not_activate when rule is constraint_only/no_direct_mapping

### 7. propagate_boundaries
- inherit mapping non-implications
- inherit node provisional status
- inherit relevant edge uncertainty
- list alternative explanations

### 8. identify_missing_information
- turn decision-critical uncertainty into open questions
- prefer asking/research/testing over guessing

### 9. produce_diagnosis
- value structure
- dominant mechanism candidates
- belief/trust gaps
- decision friction
- proof requirements
- language implications
- explicit non-inferences

### 10. handoff
- pass bounded mechanism hypotheses to S6 reasoning engine
- do not generate scientific registry updates from commercial data

## Activation semantics

- **strong_candidate** — Runtime diagnostic confidence only; not an empirical effect size.
- **candidate** — Plausible mechanism hypothesis supported by contextual evidence.
- **weak_candidate** — Exploratory hypothesis; should not drive a high-stakes strategy without verification.
- **do_not_activate** — Explicitly blocked from mechanism inference.

## Conflict rules

- Do not average contradictory customer evidence into a false middle.
- Represent segment/context heterogeneity explicitly.
- If one signal maps to multiple plausible mechanisms, keep a hypothesis set until discriminating evidence exists.
- If a mechanism hypothesis conflicts with an observed behavior, record the mismatch rather than rewriting the scientific node.
