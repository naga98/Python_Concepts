from .exceptions import InvalidInputError


class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.age = age
        self.course = str(course).strip()
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    def __str__(self):
        return (f"ID: {self.student_id:<8} Name: {self.name:<20} "
                f"Age: {self.age:<4} Course: {self.course:<15} Marks: {self.marks}")


def student_from_dict(data):
    try:
        return Student(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            marks=data["marks"],
        )
    except KeyError as exc:
        raise InvalidInputError(f"Missing field in stored record: {exc}") from exc
