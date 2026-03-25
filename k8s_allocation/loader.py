import json


def load_namespace_usage(file_path):
    """
    Load namespace-level Kubernetes usage data from a JSON file.
    """

    with open(file_path, "r") as f:
        data = json.load(f)

    return data
