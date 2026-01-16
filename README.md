# Personal Supplier Evaluation System

This repository serves as my **Personal Evaluation Engine** for white-label suppliers in massive-scale projects (World Cup).

It relies on a strict **Agent Protocol**:
1.  **I provide**: Supplier Name + Raw Context (Notes, Transcripts, Emails).
2.  **The Agent (Antigravity) provides**: A standardized, scored, and risk-assessed evaluation file.

## 📂 Core Templates

*   **[Evaluation Template (Standard)](supplier_evaluation_template.md)**: The grid that must be filled for every supplier.
*   **[System Rules](system_rules_and_outputs.md)**: The logic for Score Calculation (1-5) and Risk Flags (Critical/High).

## 🤖 Agent Protocol (How to use)

When I paste new information about a supplier:

1.  **Ingest Content**: Read all provided text/audio transcripts.
2.  **Map to Template**: Extract evidence for every block in `supplier_evaluation_template.md`.
    *   *If specific evidence is missing, mark as `[Not Informed]`.*
    *   *If a claim is made without proof, mark as `[Promise]`.*
3.  **Calculate Score**: Apply the scoring rules from `system_rules_and_outputs.md`.
4.  **Generate Output**: Create a new file in `/evaluations` (e.g., `evaluations/supplier_name.md`).
5.  **Summary**: End the response with a "Quick Summary" and "Final Recommendation".

---

## 🏆 Evaluation Criteria Summary

| Block | Focus | Critical Flag Example |
| :--- | :--- | :--- |
| **Robustness** | Scale & Uptime | < 10% of target load coverage |
| **Security** | LGPD & PenTest | Non-compliant / No Audit |
| **Roadmap** | Conflict & Agility | Shared infra with other big clients |
| **Commercial** | Pricing & Contracts | Revenue Share (Cost risk) |
