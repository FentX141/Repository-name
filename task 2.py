# TODO импортировать необходимые молули

import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as csv_file:
        with open(OUTPUT_FILENAME, 'w') as json_file:
            json_file.write(json.dumps(list(csv.DictReader(csv_file)), indent=4))

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")