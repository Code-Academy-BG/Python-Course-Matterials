"""
Build Students exam session system.
We have the below code which is working for a session with hard coded values with direct flow.

We want to make this available for different sessions, for different students group.
Feel free to organize the below code in functions.

The file should end with a single function run_session() which runs a session.
"""


import csv
import os.path
import random

from settings.testing import INPUT_DIR


SCORE_TO_PASS = 80


# The filename should be changeable as well.
with open(os.path.join(INPUT_DIR, "students_exams.csv"), "w") as source:
    writer = csv.writer(source)

    writer.writerow(
        [
            "student",
            "exam",
            "points",
        ]
    )

    # exam and student counts should be changeable
    for e in range(1, 11):
        for s in range(1, 281):
            writer.writerow(
                [
                    f"Student {s}",
                    e,
                    # Points should be also manageable
                    random.randint(random.choice([30, 40, 50]), 100),
                ],
            )


with open(os.path.join(INPUT_DIR, "students_exams.csv"), "r") as source:
    reader = csv.reader(source)
    students_data = {}

    # Add validation against the header row of the file.
    # This code should be organized as a function to allow process any file.

    for row in reader:
        if row[0] == "student":
            continue
        student_data = students_data.setdefault(
            row[0],
            {
                "student": row[0],
                "exams": {},
                "avg": 0,
            },
        )
        student_data["exams"][row[1]] = int(row[2])


for student, data in students_data.items():
    data["avg"] = sum(data["exams"].values()) // len(data["exams"])

# After having the knowledge how many passed and how many failed, please notify the headmaster
# of the facultate. The headmaster could be changed, so take care of this.

students_to_retake_exams = {
    student: {
        "should_retake": data["avg"] < SCORE_TO_PASS,
        "avg": data["avg"],
        "failed_exams": [
            exam for exam in data["exams"] if data["exams"][exam] <= SCORE_TO_PASS
        ],
    }
    for student, data in students_data.items()
}

students_passed = {}
failed_students = {}
for student, data in students_to_retake_exams.items():
    if not data["should_retake"]:
        students_passed[student] = students_data[student]
        continue

    while students_data[student]["avg"] < SCORE_TO_PASS:
        for failed_exam in data["failed_exams"]:
            for r_i in range(3):
                # Points should be also manageable
                retake_score = random.randint(random.choice([20, 30, 40, 50, 60]), 100)
                if students_data[student]["exams"][failed_exam] >= retake_score:
                    continue
                students_data[student]["exams"][failed_exam] = retake_score
                students_data[student]["avg"] = sum(
                    students_data[student]["exams"].values(),
                ) // len(students_data[student]["exams"])
                if students_data[student]["avg"] >= SCORE_TO_PASS:
                    students_passed[student] = students_data[student]
                    break
                if retake_score >= SCORE_TO_PASS:
                    break
            if students_data[student]["avg"] >= SCORE_TO_PASS:
                break
        if students_data[student]["avg"] < SCORE_TO_PASS:
            failed_students[student] = students_data[student]
            break


print(len(students_passed) + len(failed_students))
assert (
    len(students_passed) + len(failed_students) == 280
)  # This is extremely magic, should be handled


for data in sorted(
    students_passed.values(),
    key=lambda item: item["avg"],
    reverse=True,
):
    print(f"Student {data['student']} passed session with score: {data['avg']}")
    if data["student"] in students_to_retake_exams:
        print(f"Student {data['student']} passed after participation in retakes.")
        # Print out scores before retakes
        # Print out scores after retakes

# Add some info about % of students who passed the session. Print out the % who failed the session
print("\n" * 4)

for student, data in failed_students.items():
    print(f"Student {student} failed session with score: {data['avg']}")


def run_session():
    pass
