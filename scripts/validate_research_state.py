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
    modules = load("research/s1/module-lifecycle.json")
    sources = load("research/s1/source-registry.json")
    claims = load("research/s1/atomic-claims-seed.json")

    if state["protected_constraints"]["top_level_core_count"] != 7:
        errors.append("protected core count must remain 7")

    decisions = modules["modules"]
    ids = [x["id"] for x in decisions]
    if len(decisions) != 56:
        errors.append(f"expected 56 module decisions, found {len(decisions)}")
    if len(ids) != len(set(ids)):
        errors.append("duplicate module IDs")

    src_ids = [x["id"] for x in sources["sources"]]
    if len(src_ids) != len(set(src_ids)):
        errors.append("duplicate source IDs")
    known_sources = set(src_ids)

    claim_ids = [x["id"] for x in claims["claims"]]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("duplicate claim IDs")
    for c in claims["claims"]:
        missing = [s for s in c.get("source_ids", []) if s not in known_sources]
        if missing:
            errors.append(f"{c['id']} references missing sources: {missing}")

    for rel in [
        "schemas/source.schema.json",
        "schemas/uncertainty.schema.json",
        "schemas/contradiction.schema.json",
        "schemas/experiment.schema.json",
        "schemas/feedback-observation.schema.json",
        "schemas/node.schema.json",
        "schemas/scientific-edge.schema.json",
        "schemas/atomic-claim.schema.json",
        "schemas/measurement.schema.json",
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
    print("PASS: S1/S2 research-state integrity checks")
