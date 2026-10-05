#!/usr/bin/env python3
from pathlib import Path
import re, json
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/"SKILL.md"

REQUIRED=[
 "market_value/mapping-rules.json",
 "reasoning/retrieval-policy.json",
 "reasoning/conflict-catalog.json",
 "reasoning/uncertainty-policy.json",
 "reasoning/strategy-rules.json",
 "reasoning/critique-protocol.json",
 "feedback/update-policy.json",
 "feedback/update-engine.json",
 "research/registry/nodes.json",
 "research/registry/edges.json"
]

def main():
    errors=[]
    text=SKILL.read_text(encoding="utf-8")
    m=re.match(r"^---\n(.*?)\n---\n",text,re.S)
    if not m: errors.append("missing YAML frontmatter")
    fm=m.group(1) if m else ""
    if "name: copywriting-intelligence" not in fm: errors.append("wrong skill name")
    if "description:" not in fm: errors.append("missing description")
    if "TODO" in text or "PLACEHOLDER" in text: errors.append("placeholder remains")
    for p in REQUIRED:
        if not (ROOT/p).exists(): errors.append(f"missing required runtime file: {p}")
    for rel in re.findall(r"\((references/[^)]+)\)",text):
        if not (ROOT/rel).exists(): errors.append(f"missing local reference: {rel}")
    if errors:
        print("FAIL")
        for e in errors: print("-",e)
        raise SystemExit(1)
    print("PASS: copywriting-intelligence static runtime package")

if __name__=="__main__": main()
