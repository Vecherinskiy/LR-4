import json


def task(file_name: str) -> float:
    res_sum: float = 0

    with open(file_name, 'r') as file:
        data = json.load(file)

    for load_dict in data:
        product = load_dict['score'] * load_dict['weight']
        res_sum += product

    return round(res_sum, 3)

file_name_json = "input.json"
print(task(file_name_json))
