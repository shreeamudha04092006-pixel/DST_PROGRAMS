import json

def export_kpi_summary(summary_data, top_category, output_filepath):
    report = {
        "status": "SUCCESS",
        "top_category": top_category,
        "metrics": summary_data
    }

    with open(output_filepath, "w") as file:
        json.dump(report, file, indent=4)

    with open(output_filepath, "r") as file:
        return json.load(file)


summary_data = [
    {"category": "Electronics", "total_revenue": 2650.0, "avg_revenue": 1325.0},
    {"category": "Furniture", "total_revenue": 300.0, "avg_revenue": 300.0}
]

print(export_kpi_summary(summary_data, "Electronics", "kpi_report.json"))