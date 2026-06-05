from src.traffic_loader import load_traffic
from src.network_analyzer import analyze_connection
from src.anomaly_detector import detect_anomalies
from src.risk_engine import calculate_risk
from src.incident_grouper import group_incidents
from src.report_generator import generate_soc_report
from src.ticket_system import create_ticket, get_all_tickets
from src.mitre_mapper import map_to_mitre


def run():

    traffic = load_traffic()

    detection_results = []

    print("\n===== NETWORK SECURITY MONITOR =====\n")

    for record in traffic:

        analyze_connection(record)

        alerts = detect_anomalies(record)
        risk_score = calculate_risk(record, alerts)

        detection_results.append((record, alerts, risk_score))

        print(f"Source IP: {record['source_ip']}")
        print(f"Destination IP: {record['destination_ip']}")
        print(f"Protocol: {record['protocol']}")
        print(f"Port: {record['port']}")
        print(f"Connections: {record['connections']}")

        if alerts:

            print("\nAlerts:")

            for alert in alerts:

                mitre = map_to_mitre(alert)

                print(f"  [!] {alert}")
                print(
                    f"      MITRE ATT&CK: "
                    f"{mitre['technique_id']} - "
                    f"{mitre['technique_name']}"
                )

        else:
            print("\nAlerts: None")

        print(f"\nRisk Score: {risk_score}")
        print("-" * 40)

    # ==========================
    # INCIDENT CORRELATION
    # ==========================

    print("\n===== INCIDENTS =====\n")

    incidents = group_incidents(detection_results)

    for inc in incidents:

        print(f"\n🚨 INCIDENT: {inc['source_ip']}")
        print(f"Events: {inc['event_count']}")
        print(f"Total Risk: {inc['total_risk']}")

        print("Alerts:")
        print(inc.get("alerts", []))

        print("MITRE Techniques:")

        for technique in inc.get("mitre_techniques", []):
            print(f"  • {technique}")

        print("-" * 40)

    # ==========================
    # REPORT GENERATION
    # ==========================

    file_path = generate_soc_report(incidents)

    print("\n===== SOC REPORT GENERATED =====")
    print(f"Report saved to: {file_path}")

    # ==========================
    # TICKET CREATION
    # ==========================

    print("\n===== SOC INCIDENT TICKETS =====\n")

    tickets = []

    for inc in incidents:

        ticket = create_ticket(inc)
        tickets.append(ticket)

        print(f"\n🧾 TICKET CREATED")
        print(f"Ticket ID: {ticket['ticket_id']}")
        print(f"Source IP: {ticket['source_ip']}")
        print(f"Severity: {ticket['severity']}")
        print(f"Status: {ticket['status']}")
        print(f"Risk Score: {ticket['total_risk']}")

        print("MITRE Techniques:")

        for technique in ticket.get("mitre_techniques", []):
            print(f"  • {technique}")

        print("-" * 40)

    # ==========================
    # TICKET SUMMARY
    # ==========================

    print("\n===== ALL SOC TICKETS =====\n")

    all_tickets = get_all_tickets()

    for t in all_tickets:

        print(f"Ticket ID: {t['ticket_id']}")
        print(f"Source IP: {t['source_ip']}")
        print(f"Severity: {t['severity']}")
        print(f"Status: {t['status']}")
        print(f"Risk Score: {t['total_risk']}")

        print("MITRE Techniques:")

        for technique in t.get("mitre_techniques", []):
            print(f"  • {technique}")

        print("-" * 40)


if __name__ == "__main__":
    run()