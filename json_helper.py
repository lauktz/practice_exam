import json

file_path = 'cars.json'

def read_json():
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data


def save_json(cars):
    with open(file_path, 'w') as f:
        json.dump(cars, f)
