import json


def get_input_data(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        input_data = json.load(f)
    return input_data
