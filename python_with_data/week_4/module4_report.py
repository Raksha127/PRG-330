import csv


def read_sales_data(file_name):
    data = []

    with open(file_name, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data