def map_to_mitre(alert):

    mappings = {
        "Possible SSH Brute Force Attack": {
            "technique_id": "T1110",
            "technique_name": "Brute Force"
        },

        "Possible RDP Brute Force / Remote Access Abuse": {
            "technique_id": "T1021",
            "technique_name": "Remote Services"
        },

        "Possible Port Scan Activity": {
            "technique_id": "T1595",
            "technique_name": "Active Scanning"
        },

        "Possible HTTP Flood / Web Abuse": {
            "technique_id": "T1498",
            "technique_name": "Network Denial of Service"
        },

        "Possible DNS Tunneling / Abuse": {
            "technique_id": "T1071.004",
            "technique_name": "DNS Protocol"
        }
    }

    return mappings.get(
        alert,
        {
            "technique_id": "UNKNOWN",
            "technique_name": "Unknown Technique"
        }
    )