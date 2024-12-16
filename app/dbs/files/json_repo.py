import json
import os


def load_json_data(filename):
    file_path = os.path.join(os.path.dirname(__file__), '..','..','..','data', filename)
    with open(file_path, 'r') as f:
        return json.load(f)
