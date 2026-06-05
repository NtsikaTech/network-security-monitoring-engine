def analyze_connection(record):

    return {
        "source_ip": record["source_ip"],
        "destination_ip": record["destination_ip"],
        "protocol": record["protocol"],
        "port": record["port"],
        "connections": record["connections"]
    }