import csv
import os.path

from settings.testing import INPUT_DIR


def get_students_data():
    with open(os.path.join(INPUT_DIR, 'students_data.csv'), 'r') as source:
        reader = csv.reader(source)

        # Finish the function by adding code that would extract the students data from the file.
        # We only need valid students_data, i.e. from filled rows.
        pass


def get_sqrt(number):
    # This function is not working, can you fix it?
    return math.sqrt(number)


def get_top_three_students():
    # 1. Read the students_data.csv
    # 2. Collect the students data
    # 3. Return the top 3 students, ranked by current result.
    pass


def set_entry_checker():
    # Ask for user's data: First name, age and VIP status.
    # If user's age is under 18, do not allow user to proceed
    # If user's age is between 18 - 25, allow them to stay up to 11pm
    # If group 18_25 has more than 10 users, do not allow user to enter.
    # If user is aged over 25, welcome them without any additional conditions.
    # As an output print out the users count from each group, and also print the VIPs
    # Example input: (Georgi 28, VIP) OR (Alex 25)
    pass


