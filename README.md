# Supplier Evaluation System (World Cup Scale)

A standardized, high-stakes supplier evaluation system designed for massive-scale projects (e.g., World Cup prediction games with 10M+ users).

## 📂 Project Structure

- **[Supplier Schema](supplier_schema.json)**: JSON Schema defining the rigorous data model for suppliers.
- **[Evaluation Template](supplier_evaluation_template.md)**: Markdown template for manual or agent-led data collection.
- **[System Rules](system_rules_and_outputs.md)**: Logic for detecting critical risks (e.g., Lack of Auto-scaling, Missing Compliance).
- **[Automated Evaluator](evaluate_supplier.py)**: Python script that parses the data and generates a "Go/No-Go" verdict.

## 🚀 How to Use

### Option A: Automated Evaluation (Python)
1.  Fill out a JSON file following the schema (see `example_supplier_input.json`).
2.  Run the evaluator:
    ```bash
    python evaluate_supplier.py
    ```
3.  Check the generated `evaluation_report.md`.

### Option B: AI Agent Ingestion (Unstructured)
1.  Paste raw meeting notes or transcripts into the AI context.
2.  Ask the AI to "Evaluate Supplier X using the Standard Template".
3.  The agent will map the unstructured text to `supplier_evaluation_template.md` and highlight risks.

## ⚠️ Critical Risk Detection
The system automatically flags:
- 🔴 **Scale Risk**: Proven peaks < 10% of target.
- 🔴 **Infrastructure**: Lack of Auto-scaling or SLA < 99.9%.
- 🟠 **Security**: Missing PenTest or LGPD compliance.
- 🟠 **Roadmap**: High risk of conflict with other clients.

## License
MIT
