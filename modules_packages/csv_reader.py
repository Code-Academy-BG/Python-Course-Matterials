import csv


def csv_reader(filename):
    try:
        with open(filename, 'r') as source:
            reader = csv.reader(source)
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f"{filename} doesn't exists")
