#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    with open(ROOT / rel, "r", encoding="utf-8") as f:
        return json.load(f)

def unique(records, key, label, errors):
    vals=[r[key] for r in records]
    if len(vals)!=len(set(vals)):
        errors.append(f"duplicate {label} IDs")

def validate():
    errors=[]
    state=load("state/project-state.json")
    modules=load("research/s1/module-lifecycle.json")["modules"]
    sources=load("research/registry/sources.json")["sources"]
    claims=load("research/registry/claims.json")["claims"]
    nodes=load("research/registry/nodes.json")["nodes"]
    measurements=load("research/registry/measurements.json")["records"]
    contradictions=load("research/registry/contradictions.json")["records"]
    uncertainties=load("research/registry/uncertainties.json")["records"]

    if state["protected_constraints"]["top_level_core_count"] != 7:
        errors.append("protected core count must remain 7")
    if len(modules)!=56:
        errors.append(f"expected 56 modules, found {len(modules)}")

    unique(sources,"id","source",errors)
    unique(claims,"id","claim",errors)
    unique(nodes,"id","node",errors)
    unique(measurements,"id","measurement",errors)
    unique(contradictions,"id","contradiction",errors)
    unique(uncertainties,"id","uncertainty",errors)

    source_ids={x["id"] for x in sources}
    claim_ids={x["id"] for x in claims}
    node_ids={x["id"] for x in nodes}
    measurement_ids={x["id"] for x in measurements}
    uncertainty_ids={x["id"] for x in uncertainties}
    module_ids={x["id"] for x in modules}

    for c in claims:
        miss=[s for s in c.get("source_ids",[]) if s not in source_ids]
        if miss: errors.append(f"{c['id']} missing sources {miss}")
    for n in nodes:
        if n.get("parent_id") not in module_ids:
            errors.append(f"{n['id']} unknown parent {n.get('parent_id')}")
        miss=[c for c in n.get("claim_ids",[]) if c not in claim_ids]
        if miss: errors.append(f"{n['id']} missing claims {miss}")
        miss=[m for m in n.get("measurement_ids",[]) if m not in measurement_ids]
        if miss: errors.append(f"{n['id']} missing measurements {miss}")
        miss=[u for u in n.get("uncertainty_ids",[]) if u not in uncertainty_ids]
        if miss: errors.append(f"{n['id']} missing uncertainties {miss}")
    for m in measurements:
        miss=[n for n in m.get("target_ids",[]) if n not in node_ids]
        if miss: errors.append(f"{m['id']} missing target nodes {miss}")
        miss=[c for c in m.get("validity_evidence_claim_ids",[]) if c not in claim_ids]
        if miss: errors.append(f"{m['id']} missing evidence claims {miss}")
    for r in contradictions:
        miss=[c for c in r.get("claim_ids",[]) if c not in claim_ids]
        if miss: errors.append(f"{r['id']} missing claims {miss}")
        miss=[s for s in r.get("source_ids",[]) if s not in source_ids]
        if miss: errors.append(f"{r['id']} missing sources {miss}")

    covered={n["parent_id"] for n in nodes}
    missing_modules=sorted(module_ids-covered)
    if missing_modules:
        errors.append(f"uncovered modules: {missing_modules}")

    return errors

if __name__=="__main__":
    e=validate()
    if e:
        print("FAIL")
        for x in e: print("-",x)
        raise SystemExit(1)
    print("PASS: live research graph integrity")
