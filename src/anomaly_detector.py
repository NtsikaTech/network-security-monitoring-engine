def detect_anomalies(record):

    alerts = []

    port = record["port"]
    connections = record["connections"]
    protocol = record["protocol"]
    source_ip = record["source_ip"]

    # SSH Brute Force
    if port == 22 and connections > 100:
        alerts.append("Possible SSH Brute Force Attack")

    # RDP Abuse (very common SOC alert)
    if port == 3389 and connections > 80:
        alerts.append("Possible RDP Brute Force / Remote Access Abuse")

    # Port Scanning Behavior
    if connections < 10 and port in [22, 80, 443, 3389, 21]:
        alerts.append("Possible Port Scan Activity")

    # HTTP Flood / Abnormal Web Traffic
    if port == 80 and connections > 200:
        alerts.append("Possible HTTP Flood / Web Abuse")

    # DNS Abuse Simulation
    if protocol == "DNS" and connections > 150:
        alerts.append("Possible DNS Tunneling / Abuse")

    return alerts