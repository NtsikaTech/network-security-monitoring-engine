import json
from datetime import datetime

def generate_soc_report(incidents):

    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "incident_count": len(incidents),
        "incidents": incidents
    }

    file_name = f"reports/soc_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(file_name, "w") as f:
        json.dump(report, f, indent=4)

    return file_name