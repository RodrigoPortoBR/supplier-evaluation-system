# System Rules & Output Logic

This document defines how to interpret the data collected via the `Supplier Evaluation Template` and how to generate standardized outputs.

## 1. Automated Risk Flags (Red Flags)

The system parses the input data and **automatically** triggers alerts based on specific thresholds.

| Category | Flag Condition | Risk Level | Alert Message |
| :--- | :--- | :--- | :--- |
| **Scale** | `highest_participants_in_single_game` < 100k | **CRITICAL** | "No history of massive single-event scale." |
| **Scale** | `uptime_sla_percent` < 99.9% | HIGH | "SLA below industry standard for live events." |
| **Scale** | `platforms_supported.app_ios` == No | HIGH | "Missing iOS Native App." |
| **Scale** | `platforms_supported.app_android` == No | HIGH | "Missing Android Native App." |
| **Scale** | `support_in_brazil` == No | MEDIUM | "No local support time/language." |
| **Scale** | `recent_load_test_evidence` == No | HIGH | "No recent proof of load capability." |
| **Scale** | `has_auto_scaling` == No | **CRITICAL** | "Infrastructure is static; risk of crash during peaks." |
| **Security** | `lgpd_compliant` == No | **CRITICAL** | "Non-compliant with Data Privacy Laws." |
| **Security** | `has_penetration_test_report` == No | HIGH | "Security posture unverified." |
| **UX** | `mobile_responsive_score` < 7 | HIGH | "Poor mobile experience risks user churn." |
| **Product** | `real_time_updates` == No | MEDIUM | "Lag in updates will frustration users during games." |
| **Roadmap** | `conflict_risk_at_peak` == "High" | **CRITICAL** | "High risk of resource contention with other clients." |
| **Roadmap** | `dedicated_roadmap_possibility` == No | WARNING | "No guaranteed slot for urgent World Cup fixes." |
| **Integrations** | `apis_documented.partners` == No | HIGH | "Partner ecosystem integration blocked by lack of API." |
| **Commercial** | `pricing_model` == "Revenue Share" | WARNING | "Commercial model may conflict with long-term cost control." |

## 2. Recommendation Logic

Based on the aggregation of ratings and risks:

1.  **DISCARD**:
    *   IF any **CRITICAL** Risk is triggered.
    *   OR IF `Robustness` Rating < 3.
    *   OR IF `Security` Rating < 3.

2.  **PROCEED WITH CAUTION (or PoC)**:
    *   IF 0 Critical Risks.
    *   BUT > 2 HIGH Risks.
    *   OR `Team Experience` is low but `Tech` is high.

3.  **PROCEED**:
    *   IF 0 Critical Risks.
    *   AND < 2 HIGH Risks.
    *   AND Average Rating > 4.0.

## 3. Output Layers

The system generates the following outputs based on the processed inputs.

### A. Executive Summary Card (1-Pager)
*   **Header**: Supplier Name, Score (Avg of blocks), Risk Level.
*   **Key Strengths**: Top 3 rated blocks.
*   **Top Risks**: List of all triggering Red Flag messages.
*   **PMO Verdict**: One sentence summary of the `recommendation`.

### B. Comparative Matrix (For Multiple Suppliers)
*   **Rows**: Evaluation Blocks.
*   **Columns**: Suppliers.
*   **Cells**: 1-5 Rating + Critical Flags Icons (⚠️).
*   **Bottom Line**: Total Score & Estimated Cost (if provided).

### C. Risk Map
*   A categorized list of all identified risks across the evaluators, grouped by "Technical", "Business", and "Legal".

---

## Prompt Instructions (For LLM Analysis)

If using an LLM to process this evaluation:
1.  **Input**: Feed the filled `supplier_evaluation_template.md` content.
2.  **Context**: "Act as a Senior Systems Architect and PMO."
3.  **Instruction**: "Apply the logic defined in `System Rules & Output Logic`. Extract the JSON data as per `supplier_schema.json`, then generate the `Executive Summary Card`."
