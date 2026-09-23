"""Student Analytics API using FastAPI and NumPy."""

from fastapi import FastAPI, HTTPException

from analytics import (
    SUBJECTS,
    load_students,
    overall_averages,
    statistics,
    student_with_average,
    subject_averages,
)


app = FastAPI(
    title="Super30 Student Analytics API",
    description="Student performance analytics using NumPy and Plotly.",
    version="1.0.0",
)


def students_with_averages():
    students = load_students()
    return students, overall_averages(students)


@app.get("/students")
def all_students():
    return load_students()


@app.get("/student/{student_id}")
def student_details(student_id: int):
    students, averages = students_with_averages()
    for student, average in zip(students, averages):
        if student["student_id"] == student_id:
            return student_with_average(student, average)
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/average/{subject}")
def average(subject):
    if subject not in (*SUBJECTS[:2], "data-science"):
        raise HTTPException(
            status_code=404,
            detail="Subject must be python, mathematics, or data-science",
        )
    normalized_subject = "data_science" if subject == "data-science" else subject
    result = subject_averages(load_students())[normalized_subject]
    return {"subject": subject, "average": result}


@app.get("/topper")
def topper():
    students, averages = students_with_averages()
    index = int(averages.argmax())
    return student_with_average(students[index], averages[index])


@app.get("/passed")
def passed_students():
    students, averages = students_with_averages()
    passed = [
        student_with_average(student, average)
        for student, average in zip(students, averages)
        if all(student[subject] >= 40 for subject in SUBJECTS)
    ]
    return {"passing_criteria": "At least 40 marks in every subject", "students": passed}


@app.get("/failed")
def failed_students():
    students, averages = students_with_averages()
    failed = [
        student_with_average(student, average)
        for student, average in zip(students, averages)
        if any(student[subject] < 40 for subject in SUBJECTS)
    ]
    return {"passing_criteria": "At least 40 marks in every subject", "students": failed}


@app.get("/statistics")
def get_statistics():
    return statistics(load_students())


