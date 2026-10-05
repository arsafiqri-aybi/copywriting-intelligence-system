#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    with open(ROOT / rel, "r", encoding="utf-8") as f:
        return json.load(f)

def validate():
    errors = []
    state = load("state/project-state.json")
    modules = load("research/s1/module-lifecycle.json")["modules"]
    sources = load("research/registry/sources.json")["sources"]
    claims = load("research/registry/claims.json")["claims"]
    uncertainties = load("research/registry/uncertainties.json")["records"]
    candidate_map = load("research/s3/candidate-neuron-map.json")["candidates"]

    if state["protected_constraints"]["top_level_core_count"] != 7:
        errors.append("protected core count must remain 7")

    module_ids = [x["id"] for x in modules]
    if len(module_ids) != 56 or len(module_ids) != len(set(module_ids)):
        errors.append("module lifecycle must contain 56 unique stable IDs")

    src_ids = [x["id"] for x in sources]
    if len(src_ids) != len(set(src_ids)):
        errors.append("duplicate source IDs")
    known_sources = set(src_ids)

    claim_ids = [x["id"] for x in claims]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("duplicate claim IDs")
    for c in claims:
        missing = [s for s in c.get("source_ids", []) if s not in known_sources]
        if missing:
            errors.append(f"{c['id']} references missing sources: {missing}")

    neuron_ids = [x["id"] for x in candidate_map]
    if len(neuron_ids) != 280:
        errors.append(f"expected 280 breadth-first candidate neurons, found {len(neuron_ids)}")
    if len(neuron_ids) != len(set(neuron_ids)):
        errors.append("duplicate candidate neuron IDs")
    known_modules = set(module_ids)
    for n in candidate_map:
        if n["parent_id"] not in known_modules:
            errors.append(f"{n['id']} references unknown parent module {n['parent_id']}")
        if n.get("status") != "candidate":
            errors.append(f"{n['id']} must remain candidate before evidence promotion")

    unc_ids = [u["id"] for u in uncertainties]
    if len(unc_ids) != len(set(unc_ids)):
        errors.append("duplicate uncertainty IDs")

    for rel in [
        "schemas/source.schema.json","schemas/uncertainty.schema.json","schemas/contradiction.schema.json",
        "schemas/experiment.schema.json","schemas/feedback-observation.schema.json","schemas/node.schema.json",
        "schemas/scientific-edge.schema.json","schemas/atomic-claim.schema.json","schemas/measurement.schema.json",
        "research/registry/contradictions.json","research/registry/measurements.json","research/registry/edges.json",
        "research/registry/experiments.json","research/registry/feedback.json"
    ]:
        try:
            load(rel)
        except Exception as e:
            errors.append(f"{rel} invalid JSON: {e}")
    return errors

if __name__ == "__main__":
    errs = validate()
    if errs:
        print("FAIL")
        for e in errs:
            print("-", e)
        raise SystemExit(1)
    print("PASS: S1/S2/S3 bootstrap integrity")
