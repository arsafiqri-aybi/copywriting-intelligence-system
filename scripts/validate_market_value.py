#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(p):
    with open(ROOT/p,"r",encoding="utf-8") as f: return json.load(f)

def main():
    nodes=load("research/registry/nodes.json")["nodes"]
    claims=load("research/registry/claims.json")["claims"]
    edges=load("research/registry/edges.json")["records"]
    rules=load("market_value/mapping-rules.json")["rules"]
    node_ids={x["id"] for x in nodes}
    claim_ids={x["id"] for x in claims}
    edge_ids={x["id"] for x in edges}
    errs=[]
    seen=set()
    for r in rules:
        if r["id"] in seen: errs.append(f"duplicate mapping rule {r['id']}")
        seen.add(r["id"])
        for n in r.get("target_node_ids",[]):
            if n not in node_ids: errs.append(f"{r['id']} missing target node {n}")
        for c in r.get("claim_ids",[]):
            if c not in claim_ids: errs.append(f"{r['id']} missing claim {c}")
        for e in r.get("scientific_edge_ids",[]):
            if e not in edge_ids: errs.append(f"{r['id']} missing edge {e}")
        if r.get("runtime_weight") is not None:
            errs.append(f"{r['id']} illegally assigns runtime_weight")
        if r["mapping_kind"]=="no_direct_mapping" and r.get("target_node_ids"):
            errs.append(f"{r['id']} no_direct_mapping must not target nodes")
    if errs:
        print("FAIL")
        for e in errs: print("-",e)
        raise SystemExit(1)
    print(f"PASS: {len(rules)} market→mechanism rules reference live graph safely")

if __name__=="__main__": main()
