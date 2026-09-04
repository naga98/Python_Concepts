STUDENTS_FILE = "students.txt"
BACKUP_FILE = "students_backup.txt"
NAMES_COURSES_FILE = "names_courses.txt"


SAMPLE_RECORDS = [
    "101,Sudhanshu,sudh@example.com,9999999999,Python,Bangalore",
    "102,Rahul,rahul@example.com,8888888888,Data Science,Delhi",
    "103,Priya,priya@example.com,7777777777,Java,Mumbai",
    "104,Ankit,ankit@example.com,6666666666,C++,Pune",
    "105,Sneha,sneha@example.com,5555555555,Python,Hyderabad",
    "106,Karan,karan@example.com,4444444444,Web Development,Chennai",
    "107,Divya,divya@example.com,3333333333,Data Science,Kolkata",
    "108,Manoj,manoj@example.com,2222222222,Machine Learning,Bangalore",
    "109,Neha,neha@example.com,1111111111,Python,Delhi",
    "110,Suresh,suresh@example.com,9876543210,Java,Mumbai",
]


def write_records(filename=STUDENTS_FILE, records=SAMPLE_RECORDS):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for record in records:
                f.write(record + "\n")
        print(f"Wrote {len(records)} record(s) to '{filename}'.")
    except OSError as exc:
        print(f"Error writing to '{filename}': {exc}")


def append_record(record, filename=STUDENTS_FILE):
    """Append a single new student record (string) to the file."""
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(record + "\n")
        print(f"Appended record: {record}")
    except OSError as exc:
        print(f"Error appending to '{filename}': {exc}")


def read_all_records(filename=STUDENTS_FILE):
    """Read and print the entire file content at once."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(content)
        return content
        
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""


def read_individual_lines(filename=STUDENTS_FILE):
    """Read and print the file one line at a time, with line numbers."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def count_records(filename=STUDENTS_FILE):
    """Return the number of student records (non-empty lines) in the file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line for line in f if line.strip()]
        count = len(lines)
        print(f"Total records in '{filename}': {count}")
        return count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0


def copy_to_backup(source=STUDENTS_FILE, backup=BACKUP_FILE):
    """Copy all data from the source file into a backup file."""
    try:
        with open(source, "r", encoding="utf-8") as src:
            data = src.read()
        with open(backup, "w", encoding="utf-8") as dest:
            dest.write(data)
        print(f"Copied '{source}' -> '{backup}'.")
    except FileNotFoundError:
        print(f"File '{source}' not found.")
    except OSError as exc:
        print(f"Error copying to '{backup}': {exc}")


def create_names_courses_file(source=STUDENTS_FILE, filename=NAMES_COURSES_FILE):
    """Create a new file containing only the name and course of each student."""
    try:
        with open(source, "r", encoding="utf-8") as src, \
             open(filename, "w", encoding="utf-8") as dest:
            for line in src:
                line = line.strip()
                if not line:
                    continue
                fields = line.split(",")
                name = fields[1]
                course = fields[4]
                dest.write(f"{name},{course}\n")
        print(f"Created '{filename}' with names and courses.")
    except FileNotFoundError:
        print(f"File '{source}' not found.")
    except (OSError, IndexError) as exc:
        print(f"Error creating '{filename}': {exc}")


def display_menu():
    """Print the main menu options."""
    print("\n===== Student Registration Application =====")
    print("1. Write student records (create/reset file)")
    print("2. Append a new student record")
    print("3. Read complete records")
    print("4. Read individual lines")
    print("5. Count number of records")
    print("6. Copy data into backup file")
    print("7. Create names_courses.txt file")
    print("8. Exit")
    print("==============================================")


def main():
    """Main menu loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            write_records()
        elif choice == "2":
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            course = input("Course: ").strip()
            city = input("City: ").strip()
            record = f"{student_id},{name},{email},{phone},{course},{city}"
            append_record(record)
        elif choice == "3":
            read_all_records()
        elif choice == "4":
            read_individual_lines()
        elif choice == "5":
            count_records()
        elif choice == "6":
            copy_to_backup()
        elif choice == "7":
            create_names_courses_file()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
