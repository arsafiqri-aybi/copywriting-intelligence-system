#!/usr/bin/env python3
import json, sys

PERMISSIONS={
 "campaign_observation":{"audience_hypothesis","market_estimate","channel_prior","message_hypothesis","runtime_heuristic"},
 "qualitative_feedback":{"audience_hypothesis","message_hypothesis"},
 "user_research":{"audience_hypothesis","market_estimate","message_hypothesis"},
 "randomized_experiment_result":{"message_hypothesis","runtime_heuristic","calibration_parameter","scientific_claim_candidate"},
 "quasi_experiment_result":{"message_hypothesis","runtime_heuristic","calibration_parameter","scientific_claim_candidate"},
 "expert_review":{"message_hypothesis","runtime_heuristic"}
}

def decide(x):
    obs=x.get("observation_type")
    design=x.get("design")
    randomized=design in ("randomized_ab","multivariate_randomized") and x.get("valid_randomization") is True and x.get("implementation_valid") is True
    decision_valid=x.get("decision_rule_valid", True)
    if not decision_valid:
        return {"causal_variant_effect_allowed":False,"mechanism_causal_interpretation_allowed":False,"runtime_update":"invalidate","scientific_action":"none","result_class":"invalid"}
    causal_variant=randomized
    mech=causal_variant and x.get("material_components_changed",99)==1 and x.get("mechanism_identification_level") in ("L2","L3")
    primary=x.get("primary_result")
    if x.get("guardrail_result")=="worse_critical":
        update="split_by_context"; result_class="mixed"
    elif primary=="null":
        update="weaken"; result_class="null"
    elif primary=="contradicts":
        update="weaken"; result_class="contradicts"
    elif primary=="supports":
        update="strengthen"; result_class="supports"
    else:
        update="no_change"; result_class="invalid"
    requested=x.get("requested_scope")
    allowed=requested in PERMISSIONS.get(obs,set())
    scientific="create_candidate_only" if requested=="scientific_claim_candidate" and allowed and mech else "none"
    return {"causal_variant_effect_allowed":causal_variant,"mechanism_causal_interpretation_allowed":mech,"runtime_update":update if allowed else "no_change","scientific_action":scientific,"result_class":result_class}

if __name__=="__main__":
    print(json.dumps(decide(json.load(sys.stdin)),indent=2))
