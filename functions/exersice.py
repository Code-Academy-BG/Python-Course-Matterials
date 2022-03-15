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

import os
from pathlib import Path

BASE_DIR = Path(os.path.abspath(__file__)).parent.parent

INPUT_DIR = os.path.join(BASE_DIR, "test_files", "input")


class BadHeaderRow(ValueError):
    pass


HEADERS = {
    "math": ["student", "exam", "points"],
}

SCORES = {
    "math": {
        "initial_scores": [30, 40, 50],
        "retake_scores": [20, 30, 40, 50, 60],
    }
}

SCORE_TO_PASS = 80

COLORS = {
    "success": "\033[92m",
    "fail": "\033[91m",
}


def print_bold(*message):
    print("\033[1m", end="")
    print(*message)
    print("\033[21m", end="")


def print_message(color, *message):
    print(COLORS[color], end="")
    print(*message)
    print("\033[0m", end="")


def _get_file_name(discipline: str) -> str:
    return f"students_{discipline}_exams.csv"


def generate_initial_session_data(
    discipline: str,
    filename: str,
    students_count: int,
    exams_count: int,
):
    """
    Generate students session data for given discipline, student and exams count.
    :param discipline:
    :param filename:
    :param students_count:
    :param exams_count:
    :return: None, store .csv data in INPUT directory
    """

    with open(os.path.join(INPUT_DIR, filename), "w", newline="") as source:
        writer = csv.writer(source)
        writer.writerow(
            [
                "student",
                "exam",
                "points",
            ],
        )

        for e in range(1, exams_count + 1):
            for s in range(1, students_count + 1):
                writer.writerow(
                    [
                        f"Student {s}",
                        e,
                        # Points should be also manageable
                        random.randint(
                            random.choice(SCORES[discipline]["initial_scores"]),
                            100,
                        ),
                    ],
                )


def read_session_data(filename: str, discipline: str) -> dict:
    with open(os.path.join(INPUT_DIR, filename), "r") as source:
        reader = csv.reader(source)
        students_data = {}

        header_row = next(reader)
        if header_row != HEADERS[discipline]:
            raise BadHeaderRow(
                f"Header row not matching the expected for {discipline}."
                f" {header_row} != {HEADERS[discipline]}."
            )

        for student, exam, points in reader:
            if student == "student":
                continue
            student_data = students_data.setdefault(
                student,
                {
                    "student": student,
                    "exams": {},
                    "avg": 0,
                },
            )
            student_data["exams"][exam] = int(points)
    return students_data


def update_avg(students_data: dict):
    for student, data in students_data.items():
        data["avg"] = sum(data["exams"].values()) // len(data["exams"])


def notify_headmaster_about_retakes_count(students_data: dict):
    retakes = sum(
        1 for student in students_data.values() if student["avg"] < SCORE_TO_PASS
    )
    print_bold(f"Headmaster, we have {retakes} students that need to retake exams")
    print("\n" * 3)


def _retake(data, exam, students_passed, retakes_data, discipline):
    for r_i in range(3):
        retake_score = random.randint(
            random.choice(SCORES[discipline]["initial_scores"]),
            100,
        )
        if data["exams"][exam] >= retake_score:
            continue
        student_retakes_data = retakes_data.setdefault(data["student"], {})
        exam_data = student_retakes_data.setdefault(exam, {"before": [], "after": []})
        exam_data["before"].append(data["exams"][exam])
        exam_data["after"].append(retake_score)
        data["exams"][exam] = retake_score
        data["avg"] = sum(data["exams"].values()) // len(data["exams"])
        if data["avg"] >= SCORE_TO_PASS:
            students_passed[data["student"]] = data
            break
        if retake_score >= SCORE_TO_PASS:
            break


def handle_retakes(students_data, discipline):
    print_bold("=" * 10, "START retakes", "=" * 10)
    students_passed = {}
    failed_students = {}
    retakes_data = {}
    for student, data in students_data.items():
        print_bold(f"Student {student} start retake!")
        if data["avg"] >= SCORE_TO_PASS:
            students_passed[student] = data
            continue

        while data["avg"] < SCORE_TO_PASS:
            failed_exams = [
                e for e in data["exams"] if data["exams"][e] < SCORE_TO_PASS
            ]
            for exam in failed_exams:
                _retake(data, exam, students_passed, retakes_data, discipline)
                if data["avg"] >= SCORE_TO_PASS:
                    print_message("success", f"Student {student} passed retake :)")
                    break
            if data["avg"] < SCORE_TO_PASS:
                print_message("fail", f"Student {student} failed retake :(")
                failed_students[student] = data
                break
    print_bold("=" * 10, "END retakes", "=" * 10)
    return students_passed, failed_students, retakes_data


def notify_results(students_passed, failed_students, retakes_data):
    for data in sorted(
        students_passed.values(),
        key=lambda item: item["avg"],
        reverse=True,
    ):
        print_message(
            "success",
            f"Student {data['student']} passed session with score: {data['avg']}",
        )
        if data["student"] in retakes_data:
            print_message(
                "success",
                f"Student {data['student']} passed after participation in retakes.",
            )
            for exam, exam_data in retakes_data[data["student"]].items():
                print(" " * 4, f"Exam {exam} data")
                for idx, e in enumerate(exam_data["before"]):
                    print(
                        " " * 4,
                        f"exam {exam} before {e}, after: {exam_data['after'][idx]}",
                    )

    print("\n" * 4)

    for student, data in failed_students.items():
        print_message(
            "fail",
            f"Student {student} failed session with score: {data['avg']}",
        )


def run_session(discipline):
    generate_initial_session_data(discipline, _get_file_name(discipline), 220, 5)
    students_data = read_session_data(_get_file_name(discipline), discipline)
    update_avg(students_data)
    notify_headmaster_about_retakes_count(students_data)
    passed, failed, retakes_data = handle_retakes(students_data, discipline)
    assert len(passed) + len(failed) == len(students_data)
    notify_results(passed, failed, retakes_data)


run_session("math")
