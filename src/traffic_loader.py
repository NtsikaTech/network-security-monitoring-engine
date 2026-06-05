import json

def load_traffic():

    with open("data/sample_traffic.json", "r") as file:
        return json.load(file)