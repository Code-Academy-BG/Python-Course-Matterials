import csv
import os

from settings.testing import INPUT_DIR

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruits)

# In other words:
# for var in iterable:
#     do something


for fruit in fruits:
    if len(fruit) < 3:
        continue
        # break
    elif len(fruit) > 100000:
        continue
    else:
        print(fruit)
        # break This would cause an immediate exit from the loop
else:
    print("CodeAcademy")

# for x in range(99):
#     print("X", x)

print(INPUT_DIR)
with open(os.path.join(INPUT_DIR, 'students_data.csv'), 'r') as source:
    reader = csv.reader(source)
    print(reader)

    for row in reader:
        print(row)

    print("Before second attempt to read reader")
    for row in reader:
        print(row)
