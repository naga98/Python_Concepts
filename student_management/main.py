import logging

from .logger_config import setup_logger
from .file_handler import save_students, load_students
from .operations import (
    add_student,
    remove_student,
    update_student,
    search_student,
    display_all_students,
)
from .exceptions import StudentManagementError

logger = setup_logger()


def display_menu():
    """Print the main menu options to the console."""
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Save & Exit")
    print("=======================================")


def get_menu_choice():
    return input("Enter your choice (1-6): ").strip()


def handle_add(students):
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")
        student = add_student(students, student_id, name, age, course, marks)
        print(f"Student added successfully:\n{student}")
    except StudentManagementError as exc:
        print(f"Error: {exc}")
        logger.error("Add student failed: %s", exc)


def handle_remove(students):
    """Prompt for a student ID and remove that record."""
    try:
        student_id = input("Enter Student ID to remove: ")
        student = remove_student(students, student_id)
        print(f"Removed student:\n{student}")
    except StudentManagementError as exc:
        print(f"Error: {exc}")
        logger.error("Remove student failed: %s", exc)


def handle_update(students):
    """Prompt for updated fields (blank = keep current value) and update the record."""
    try:
        student_id = input("Enter Student ID to update: ")
        print("Leave a field blank to keep its current value.")
        name = input("New Name: ").strip() or None
        age = input("New Age: ").strip() or None
        course = input("New Course: ").strip() or None
        marks = input("New Marks: ").strip() or None
        student = update_student(students, student_id, name, age, course, marks)
        print(f"Student updated successfully:\n{student}")
    except StudentManagementError as exc:
        print(f"Error: {exc}")
        logger.error("Update student failed: %s", exc)


def handle_search(students):
    """Prompt for a search term (ID or name) and print matching students."""
    try:
        mode = input("Search by (1) ID or (2) Name? Enter 1 or 2: ").strip()
        if mode == "1":
            student_id = input("Enter Student ID: ")
            results = search_student(students, student_id=student_id)
        elif mode == "2":
            name = input("Enter Name (or part of it): ")
            results = search_student(students, name=name)
        else:
            print("Invalid option selected.")
            return

        if results:
            print(f"Found {len(results)} matching student(s):")
            for s in results:
                print(s)
        else:
            print("No matching student found.")
    except StudentManagementError as exc:
        print(f"Error: {exc}")
        logger.error("Search student failed: %s", exc)


def handle_display(students):
    """Print all students currently stored."""
    all_students = display_all_students(students)
    if not all_students:
        print("No students to display.")
        return
    print(f"\nTotal students: {len(all_students)}")
    for s in all_students:
        print(s)


def main():
    logger.info("===== Student Management System started. =====")
    try:
        students = load_students()
    except StudentManagementError as exc:
        print(f"Warning: could not load existing data ({exc}). Starting with an empty list.")
        students = {}

    actions = {
        "1": handle_add,
        "2": handle_remove,
        "3": handle_update,
        "4": handle_search,
        "5": handle_display,
    }

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "6":
            try:
                save_students(students)
                print("Data saved. Goodbye!")
            except StudentManagementError as exc:
                print(f"Error saving data: {exc}")
                logger.error("Final save failed: %s", exc)
            break
        elif choice in actions:
            actions[choice](students)
            # Persist after every successful mutating/search operation.
            try:
                save_students(students)
            except StudentManagementError as exc:
                print(f"Warning: could not auto-save data ({exc}).")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            logger.warning("Invalid menu choice entered: '%s'.", choice)

    logger.info("===== Student Management System stopped. =====")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
        logger.warning("Program interrupted by user (KeyboardInterrupt).")
    except Exception as exc:  # last-resort safety net for truly unexpected errors
        print(f"An unexpected error occurred: {exc}")
        logger.critical("Unhandled exception: %s", exc, exc_info=True)
