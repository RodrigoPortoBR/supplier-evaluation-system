# Supplier Evaluation System - Walkthrough

This document demonstrates how to use the newly created Supplier Evaluation System.

## System Components (Deliverables)

1.  **[Data Schema (JSON)](file:///C:/Users/rodri/.gemini/antigravity/brain/c02acd62-85f8-4299-96d2-99cdc92c6808/supplier_schema.json)**: The technical backbone for validating data.
2.  **[Evaluation Template (Markdown)](file:///C:/Users/rodri/.gemini/antigravity/brain/c02acd62-85f8-4299-96d2-99cdc92c6808/supplier_evaluation_template.md)**: The "Form" for human evaluators.
3.  **[Rules & Output Logic](file:///C:/Users/rodri/.gemini/antigravity/brain/c02acd62-85f8-4299-96d2-99cdc92c6808/system_rules_and_outputs.md)**: The "Brain" for analyzing results.

---

## Mock Verification Scenario

To verify the system, we applied it to a hypothetical supplier: **"BetTech Solutions (Hypothetical)"**.

### 1. The Input (Simulated)
*Reviewing key fields from a filled template:*

*   **Robustness**:
    *   `max_concurrent_users_tested`: 50,000 (Target is 500,000)
    *   `uptime_sla_percent`: 99.5%
    *   `has_auto_scaling`: Yes
*   **Security**:
    *   `lgpd_compliant`: Yes
    *   `has_penetration_test_report`: No
*   **Commercial**:
    *   `pricing_model`: "Revenue Share"

### 2. The Analysis (Applying Rules)

Using `system_rules_and_outputs.md`:

#### Detected Risks (Red Flags)
1.  **CRITICAL RISK**: `max_concurrent_users_tested` (50k) is < 10% of Projected Audience.
    *   *Rule: "Proven scale insufficient for target audience."*
2.  **HIGH RISK**: `uptime_sla_percent` (99.5%) is < 99.9%.
    *   *Rule: "SLA below industry standard for live events."*
3.  **HIGH RISK**: `has_penetration_test_report` is No.
    *   *Rule: "Security posture unverified."*
4.  **WARNING**: `pricing_model` is "Revenue Share".
    *   *Rule: "Commercial model may conflict with long-term cost control."*

### 3. Generated Output

**Assessment:**
*   **Critical Risks**: 1
*   **High Risks**: 2
*   **Recommendation**: **DISCARD** (Triggered by Critical Risk on Scale).

## Automated Evaluation Tool

I have built a Python script to automate this entire process.

### How to use
1.  **Prepare Data**: Create a JSON file (e.g., `supplier_data.json`) following the [Schema](supplier_schema.json).
2.  **Run Script**:
    ```bash
    python evaluate_supplier.py
    ```
    *(Note: The script currently defaults to reading `example_supplier_input.json`. You can modify the script to accept arguments or change the filename variable.)*

### Output
The tool will generate `evaluation_report.md` containing:
- Executive Summary
- Risk Matrix
- Final PMO Verdict

## Workflow B: Unstructured Ingestion (Agent-Led)

If you have raw notes, transcripts, or emails:

1.  **Send Content**: Paste the text (or attach transcript files) into this chat.
    *   *Note: For audio files, please provide the transcript.*
2.  **Instruction**: Tell me "Use this to evaluate [Supplier Name]".
3.  **Process**: I will analyze the text, extract evidence, and generate a filled **[Supplier Evaluation Template](supplier_evaluation_template.md)** for you.
4.  **Review**: You simply verify the filled markdown file I generate.

---

## Conclusion

The system successfully:
1.  Captured structured data ensuring no blocks were missed.
2.  Identified specific fatal flaws (Scale) that might be hidden in sales pitches.
3.  Generated a clear, defensible "DISCARD" recommendation based on objective rules.
