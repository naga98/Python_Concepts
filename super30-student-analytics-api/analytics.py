"""Shared student data loading and NumPy analytics."""

import csv
from pathlib import Path

import numpy as np


DATA_FILE = Path(__file__).with_name("students.csv")
SUBJECTS = ("python", "mathematics", "data_science")


def load_students():
    """Load the CSV dataset as JSON-friendly Python dictionaries."""
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        return [
            {
                "student_id": int(row["student_id"]),
                "name": row["name"],
                "python": int(row["python"]),
                "mathematics": int(row["mathematics"]),
                "data_science": int(row["data_science"]),
            }
            for row in csv.DictReader(file)
        ]


def marks_array(students):
    return np.array([[student[subject] for subject in SUBJECTS] for student in students])


def overall_averages(students):
    return np.mean(marks_array(students), axis=1)


def student_with_average(student, average):
    result = dict(student)
    result["overall_average"] = round(float(average), 2)
    return result


def subject_averages(students):
    averages = np.mean(marks_array(students), axis=0)
    return {subject: round(float(value), 2) for subject, value in zip(SUBJECTS, averages)}


def statistics(students):
    marks = marks_array(students)
    averages = overall_averages(students)
    return {
        "subject_averages": subject_averages(students),
        "highest_marks": {
            subject: int(np.max(marks[:, index]))
            for index, subject in enumerate(SUBJECTS)
        },
        "lowest_marks": {
            subject: int(np.min(marks[:, index]))
            for index, subject in enumerate(SUBJECTS)
        },
        "overall_average": round(float(np.mean(averages)), 2),
    }
