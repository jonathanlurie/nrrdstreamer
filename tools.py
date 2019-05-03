import json

def pretty_print(payload):
    """
    This helper function display a Python dict in a nice way, using the JSON syntax and an indentation of 2.
    :param payload: A Python dict
    """
    print(json.dumps(payload, indent=2))

def to_json(payload):
    return json.dumps(payload, indent=2)
