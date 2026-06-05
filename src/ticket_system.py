import uuid
from datetime import datetime

TICKETS = []

def create_ticket(incident):

    severity = "LOW"

    if incident["total_risk"] > 200:
        severity = "CRITICAL"
    elif incident["total_risk"] > 120:
        severity = "HIGH"
    elif incident["total_risk"] > 60:
        severity = "MEDIUM"

    ticket = {
        "ticket_id": str(uuid.uuid4())[:8],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "OPEN",
        "severity": severity,
        "source_ip": incident["source_ip"],
        "event_count": incident["event_count"],
        "alerts": incident["alerts"],
        "total_risk": incident["total_risk"]
    }

    TICKETS.append(ticket)
    return ticket


def get_all_tickets():
    return TICKETS


def close_ticket(ticket_id):

    for t in TICKETS:
        if t["ticket_id"] == ticket_id:
            t["status"] = "CLOSED"
            t["closed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return t

    return None