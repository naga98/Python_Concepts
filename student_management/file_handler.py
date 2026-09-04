import json
import os
import logging

from .student import student_from_dict
from .exceptions import FileOperationError

logger = logging.getLogger("student_management")

DATA_FILE = os.path.join(os.getcwd(), "students_data.json")


def save_students(students, filename=DATA_FILE):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in students.values()], f, indent=4)
        logger.info("Saved %d student record(s) to '%s'.", len(students), filename)
    except (IOError, OSError, TypeError) as exc:
        logger.error("Failed to save data to '%s': %s", filename, exc)
        raise FileOperationError(f"Could not save data to file: {exc}") from exc


def load_students(filename=DATA_FILE):
    students = {}
    if not os.path.exists(filename):
        logger.info("No existing data file found at '%s'. Starting fresh.", filename)
        return students

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                logger.warning("Data file '%s' is empty.", filename)
                return students
            raw_list = json.loads(content)

        for raw in raw_list:
            student = student_from_dict(raw)
            students[student.student_id] = student

        logger.info("Loaded %d student record(s) from '%s'.", len(students), filename)
        return students
    except (IOError, OSError) as exc:
        logger.error("Failed to read data file '%s': %s", filename, exc)
        raise FileOperationError(f"Could not read data file: {exc}") from exc
    except json.JSONDecodeError as exc:
        logger.error("Corrupted data file '%s': %s", filename, exc)
        raise FileOperationError(f"Data file is corrupted: {exc}") from exc
