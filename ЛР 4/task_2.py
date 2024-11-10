import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
        csv_dicts_reader = csv.DictReader(input_file)

        list_dicts = [csv_dict for csv_dict in csv_dicts_reader]

        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
            json.dump(list_dicts, output_file, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
