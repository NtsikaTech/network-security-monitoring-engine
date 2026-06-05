from collections import defaultdict
from src.mitre_mapper import map_to_mitre


def group_incidents(detection_results):

    incidents = defaultdict(list)

    for record, alerts, risk in detection_results:

        source_ip = record["source_ip"]

        incidents[source_ip].append({
            "port": record["port"],
            "protocol": record["protocol"],
            "connections": record["connections"],
            "alerts": alerts,
            "risk_score": risk
        })

    grouped_incidents = []

    for ip, events in incidents.items():

        total_risk = sum(e["risk_score"] for e in events)

        all_alerts = []
        all_mitre = []

        for e in events:

            all_alerts.extend(e["alerts"])

            # 🔥 MITRE mapping per alert
            for alert in e["alerts"]:

                mitre = map_to_mitre(alert)

                all_mitre.append(
                    f"{mitre['technique_id']} - {mitre['technique_name']}"
                )

        grouped_incidents.append({
            "source_ip": ip,
            "event_count": len(events),
            "total_risk": total_risk,
            "alerts": list(set(all_alerts)),
            "mitre_techniques": list(set(all_mitre))
        })

    return grouped_incidents