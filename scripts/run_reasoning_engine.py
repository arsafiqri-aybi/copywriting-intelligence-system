#!/usr/bin/env python3
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(p):
    with open(ROOT/p,"r",encoding="utf-8") as f: return json.load(f)

def resolve_signals(signals, rules):
    activated={}
    matched=[]
    for s in signals:
        for r in rules:
            p=r["signal_pattern"]
            if p["dimension"]==s.get("dimension") and s.get("fact_type") in p.get("fact_types",[]):
                matched.append(r["id"])
                if r.get("activation_effect")=="do_not_activate":
                    continue
                for nid in r.get("target_node_ids",[]):
                    current=activated.get(nid, {"rule_ids":[],"rule_statuses":[],"basis":[]})
                    current["rule_ids"].append(r["id"])
                    current["rule_statuses"].append(r["status"])
                    current["basis"].append(f"{s.get('dimension')}:{s.get('fact_type')}")
                    activated[nid]=current
    return activated, sorted(set(matched))

def activation_status(meta, node_status):
    statuses=set(meta["rule_statuses"])
    if node_status=="provisional" or "provisional" in statuses or "heuristic" in statuses:
        return "weak_candidate"
    if len(set(meta["rule_ids"]))>=2:
        return "strong_candidate"
    return "candidate"

def retrieve(seed_ids, edges):
    retrieved_nodes=set(seed_ids)
    retrieved_edges=[]
    for e in edges:
        if e["source"] in seed_ids or e["target"] in seed_ids:
            if e["status"] in ("accepted","provisional"):
                retrieved_edges.append(e["id"])
                retrieved_nodes.add(e["source"]); retrieved_nodes.add(e["target"])
    return sorted(retrieved_nodes), sorted(set(retrieved_edges))

def detect_conflicts(active_ids, conflicts):
    aset=set(active_ids)
    out=[]
    for c in conflicts:
        if set(c["participants"]).issubset(aset):
            out.append(c["id"])
    return out

def select_strategies(active_ids, conflict_ids, rules):
    aset=set(active_ids); cset=set(conflict_ids); out=[]
    for r in rules:
        if set(r.get("when_nodes",[])).issubset(aset) and set(r.get("when_conflicts",[])).issubset(cset):
            out.append(r["id"])
    return out

def run(signals):
    mappings=load("market_value/mapping-rules.json")["rules"]
    nodes=load("research/registry/nodes.json")["nodes"]
    edges=load("research/registry/edges.json")["records"]
    conflicts=load("reasoning/conflict-catalog.json")["conflicts"]
    strategies=load("reasoning/strategy-rules.json")["rules"]
    nmap={n["id"]:n for n in nodes}
    seeds, matched=resolve_signals(signals,mappings)
    ledger=[]
    for nid,meta in seeds.items():
        ns=nmap[nid]["status"]
        ledger.append({"node_id":nid,"role":"primary","runtime_status":activation_status(meta,ns),"basis":meta["basis"],"mapping_rule_ids":meta["rule_ids"],"evidence_state":"provisional" if ns=="provisional" else "accepted_direct"})
    active=[x["node_id"] for x in ledger if x["runtime_status"]!="blocked"]
    rnodes,redges=retrieve(active,edges)
    cids=detect_conflicts(active,conflicts)
    sids=select_strategies(active,cids,strategies)
    return {"matched_mapping_rules":matched,"activation_ledger":ledger,"seed_node_ids":sorted(active),"retrieved_node_ids":rnodes,"retrieved_edge_ids":redges,"conflict_ids":cids,"strategy_rule_ids":sids}

if __name__=="__main__":
    if len(sys.argv)>1:
        inp=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    else:
        inp=json.load(sys.stdin)
    print(json.dumps(run(inp.get("signals",[])),indent=2))
