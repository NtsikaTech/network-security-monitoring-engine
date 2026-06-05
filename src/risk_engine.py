def calculate_risk(record, alerts):

    score = 0

    port = record["port"]
    connections = record["connections"]

    # Base risk from connections
    if connections > 250:
        score += 50
    elif connections > 100:
        score += 30
    elif connections > 50:
        score += 15
    else:
        score += 5

    # Port-based risk weighting
    if port == 22:
        score += 25  # SSH
    elif port == 3389:
        score += 25  # RDP
    elif port == 80:
        score += 10  # HTTP
    elif port == 53:
        score += 20  # DNS

    # Alert-based risk boost
    score += len(alerts) * 15

    # Cap score
    if score > 100:
        score = 100

    return score