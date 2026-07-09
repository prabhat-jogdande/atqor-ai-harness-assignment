import json


def load_examples():

    with open("prompts/examples/examples.json") as f:
        return json.load(f)