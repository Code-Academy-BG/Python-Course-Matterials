import os

from modules_packages.csv_reader import csv_reader
from settings.testing import INPUT_DIR

for row in csv_reader(os.path.join(INPUT_DIR, 'students_data.csv')):
    print(row)
