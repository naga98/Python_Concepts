import logging

from .student import Student
from .exceptions import (
    StudentNotFoundError,
    DuplicateStudentError,
    InvalidInputError,
)

logger = logging.getLogger("student_management")


def validate_student_data(student_id, name, age, course, marks):
    if not student_id or not str(student_id).strip():
        raise InvalidInputError("Student ID cannot be empty.")
    if not name or not str(name).strip():
        raise InvalidInputError("Student name cannot be empty.")
    try:
        age = int(age)
        if age <= 0 or age > 120:
            raise InvalidInputError("Age must be a realistic positive number.")
    except (ValueError, TypeError) as exc:
        raise InvalidInputError("Age must be a valid integer.") from exc
    if not course or not str(course).strip():
        raise InvalidInputError("Course cannot be empty.")
    try:
        marks = float(marks)
        if marks < 0 or marks > 100:
            raise InvalidInputError("Marks must be between 0 and 100.")
    except (ValueError, TypeError) as exc:
        raise InvalidInputError("Marks must be a valid number.") from exc
    return age, marks


def get_student_by_id(students, student_id):
    student_id = str(student_id).strip()
    if student_id not in students:
        raise StudentNotFoundError(f"No student found with ID '{student_id}'.")
    return students[student_id]


def add_student(students, student_id, name, age, course, marks):
    student_id = str(student_id).strip()
    if student_id in students:
        logger.warning("Attempted to add duplicate student ID '%s'.", student_id)
        raise DuplicateStudentError(f"Student with ID '{student_id}' already exists.")

    age, marks = validate_student_data(student_id, name, age, course, marks)
    students[student_id] = Student(student_id, name, age, course, marks)
    logger.info("Added student '%s' (ID: %s).", name, student_id)
    return students[student_id]


def remove_student(students, student_id):
    student = get_student_by_id(students, student_id)
    del students[student.student_id]
    logger.info("Removed student '%s' (ID: %s).", student.name, student.student_id)
    return student


def update_student(students, student_id, name=None, age=None, course=None, marks=None):
    student = get_student_by_id(students, student_id)

    new_name = name if name is not None and str(name).strip() else student.name
    new_age = age if age is not None else student.age
    new_course = course if course is not None and str(course).strip() else student.course
    new_marks = marks if marks is not None else student.marks

    validated_age, validated_marks = validate_student_data(
        student.student_id, new_name, new_age, new_course, new_marks
    )

    student.name = str(new_name).strip()
    student.age = validated_age
    student.course = str(new_course).strip()
    student.marks = validated_marks

    logger.info("Updated student (ID: %s).", student.student_id)
    return student


def search_student(students, student_id=None, name=None):
    results = []
    if student_id:
        try:
            results.append(get_student_by_id(students, student_id))
        except StudentNotFoundError:
            results = []
    elif name:
        name_lower = str(name).strip().lower()
        results = [s for s in students.values() if name_lower in s.name.lower()]
    else:
        raise InvalidInputError("Provide either a student ID or a name to search.")

    logger.info("Search performed (id=%s, name=%s) -> %d result(s).",
                student_id, name, len(results))
    return results


def get_student_id(student):
    return student.student_id


def display_all_students(students):
    ordered = sorted(students.values(), key=get_student_id)
    logger.info("Displayed all students (%d record(s)).", len(ordered))
    return ordered
