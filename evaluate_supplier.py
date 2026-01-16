import json
import statistics
from datetime import datetime

# Load the schema to ensure we know the structure (in a real app we'd validate against it)
# For this script we will assume the input json matches the schema structure.

def evaluate_supplier(supplier_data):
    """
    Analyzes supplier data against the System Rules.
    Returns a dictionary with risks, scores, and recommendation.
    """
    risks = []
    scores = []
    
    # helper to add risk
    def add_risk(category, level, message):
        risks.append({
            "category": category,
            "level": level,
            "message": message
        })

    # --- 1. Robustness & Scale ---
    rb = supplier_data.get("evaluation_blocks", {}).get("robustness_scale", {})
    scores.append(rb.get("block_rating", 0))
    
    if rb.get("highest_participants_in_single_game", 0) < 100000:
        add_risk("Scale", "CRITICAL", "No history of massive single-event scale (<100k).")
    
    if rb.get("uptime_sla_percent", 100) < 99.9:
        add_risk("Scale", "HIGH", "SLA below industry standard for live events (<99.9%).")
        
    platforms = rb.get("platforms_supported", {})
    if not platforms.get("app_ios"):
        add_risk("Scale", "HIGH", "Missing iOS Native App.")
    if not platforms.get("app_android"):
        add_risk("Scale", "HIGH", "Missing Android Native App.")
        
    if not rb.get("support_in_brazil"):
        add_risk("Scale", "MEDIUM", "No local support time/language.")
        
    if not rb.get("has_auto_scaling"):
        add_risk("Scale", "CRITICAL", "Infrastructure is static; risk of crash during peaks.")

    # --- 2. Security ---
    sec = supplier_data.get("evaluation_blocks", {}).get("security_governance", {})
    scores.append(sec.get("block_rating", 0))
    
    if not sec.get("lgpd_compliant"):
        add_risk("Security", "CRITICAL", "Non-compliant with Data Privacy Laws (LGPD).")
        
    if not sec.get("has_penetration_test_report"):
        add_risk("Security", "HIGH", "Security posture unverified (No PenTest).")

    # --- 3. Core Features ---
    prod = supplier_data.get("evaluation_blocks", {}).get("core_features", {})
    scores.append(prod.get("block_rating", 0))
    
    # Check for real-time capabilities
    if not prod.get("real_time_data_api", {}).get("live_data_display", False): 
        add_risk("Product", "MEDIUM", "No real-time data display capability.")

    # --- 4. Customization ---
    ux = supplier_data.get("evaluation_blocks", {}).get("customization_ux", {})
    scores.append(ux.get("block_rating", 0))
    
    if ux.get("mobile_responsive_score", 10) < 7:
        add_risk("UX", "HIGH", "Poor mobile experience risks user churn.")

    # --- 5. Roadmap ---
    road = supplier_data.get("evaluation_blocks", {}).get("roadmap_evolution", {})
    scores.append(road.get("block_rating", 0))
    
    if road.get("conflict_risk_at_peak") == "High":
        add_risk("Roadmap", "CRITICAL", "High risk of resource contention with other clients.")
        
    if not road.get("dedicated_roadmap_possibility"):
        add_risk("Roadmap", "WARNING", "No guaranteed slot for urgent World Cup fixes.")

    # --- 6. Integrations ---
    integ = supplier_data.get("evaluation_blocks", {}).get("integrations", {})
    scores.append(integ.get("block_rating", 0))
    
    if not integ.get("apis_documented", {}).get("partners"):
        add_risk("Integrations", "HIGH", "Partner ecosystem integration blocked by lack of API.")

    # --- 7, 8, 9, 10 Other Blocks (Just scoring for now) ---
    scores.append(supplier_data.get("evaluation_blocks", {}).get("channels_notifications", {}).get("block_rating", 0))
    scores.append(supplier_data.get("evaluation_blocks", {}).get("social_virality", {}).get("block_rating", 0))
    
    comm = supplier_data.get("evaluation_blocks", {}).get("commercial_contractual", {})
    scores.append(comm.get("block_rating", 0))
    if comm.get("pricing_model") == "Revenue Share":
        add_risk("Commercial", "WARNING", "Pricing model (RevShare) conflicts with cost control.")
        
    team = supplier_data.get("evaluation_blocks", {}).get("team_references", {})
    scores.append(team.get("block_rating", 0))
    
    if team.get("previous_world_cup_cases", 0) == 0:
        add_risk("Team", "MEDIUM", "Supplier unverified in massive sports events.")

    # --- Analysis ---
    avg_score = statistics.mean([s for s in scores if s > 0]) # Ignore 0s if any
    
    critical_risks = [r for r in risks if r["level"] == "CRITICAL"]
    high_risks = [r for r in risks if r["level"] == "HIGH"]
    
    recommendation = "PROCEED"
    if critical_risks:
        recommendation = "DISCARD"
    elif len(high_risks) > 2:
        recommendation = "PROCEED WITH CAUTION"
    elif avg_score < 3.0:
        recommendation = "DISCARD"
        
    return {
        "supplier": supplier_data.get("supplier_info", {}).get("name"),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "avg_score": round(avg_score, 2),
        "risks": risks,
        "recommendation": recommendation,
        "counts": {
            "critical": len(critical_risks),
            "high": len(high_risks),
            "medium": len([r for r in risks if r["level"] == "MEDIUM"]),
            "warning": len([r for r in risks if r["level"] == "WARNING"])
        }
    }

def generate_report_markdown(analysis):
    md = f"""# Executive Summary: {analysis['supplier']}
**Date:** {analysis['date']}
**PMO Verdict:** {analysis['recommendation']}
**Average Technical Score:** {analysis['avg_score']} / 5.0

## Risk Profile
- **CRITICAL:** {analysis['counts']['critical']}
- **HIGH:** {analysis['counts']['high']}
- **MEDIUM:** {analysis['counts']['medium']}

## Detected Risks
"""
    if not analysis['risks']:
        md += "No significant risks detected.\n"
    else:
        for r in analysis['risks']:
            icon = "🔴" if r['level'] == "CRITICAL" else "🟠" if r['level'] == "HIGH" else "🟡"
            md += f"- {icon} **[{r['level']}]** {r['category']}: {r['message']}\n"
            
    return md

if __name__ == "__main__":
    # In a real scenario, we would load this from a file argument
    input_file = "example_supplier_input.json"
    
    try:
        with open(input_file, "r", encoding='utf-8') as f:
            data = json.load(f)
            
        result = evaluate_supplier(data)
        report = generate_report_markdown(result)
        
        # Save report with explicit utf-8
        with open("evaluation_report.md", "w", encoding='utf-8') as f:
            f.write(report)
            
        print("Evaluation complete. Report saved to 'evaluation_report.md'.")
        # safely print preview (replacing chars if needed for terminal)
        try:
             print(report)
        except UnicodeEncodeError:
             print(report.encode('ascii', 'replace').decode('ascii'))
            
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please create it first.")
    except Exception as e:
        print(f"Error processing evaluation: {e}")
