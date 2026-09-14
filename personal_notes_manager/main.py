NOTES_FILE = "notes.txt"


def main():
    initial_notes = [
        "Buy groceries",
        "Finish the Python assignment",
        "Call Alex",
        "Read for 30 minutes",
        "Plan the weekend",
        "Back up important files",
        "Practice file handling",
        "Review today's tasks",
        "Prepare tomorrow's schedule",
        "Take a short break",
    ]

    # w creates the file or replaces its contents.
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(initial_notes) + "\n")
    print(f"Created {NOTES_FILE} and wrote {len(initial_notes)} lines.")

    # r reads the entire file and closes it automatically.
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        entire_contents = file.read()
    print("\nEntire file:")
    print(entire_contents, end="")

    # read() can receive a character limit.
    file = open(NOTES_FILE, "r", encoding="utf-8")
    character_sample = file.read(25)
    file.close()
    print("\nFirst 25 characters:")
    print(repr(character_sample))
    print("File closed explicitly:", file.closed)

    # readline() reads one line.
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        first_line = file.readline()
    print("\nUsing readline():")
    print(first_line, end="")

    # readlines() returns all lines as a list.
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
    print("\nUsing readlines():")
    for line_number, line in enumerate(lines, start=1):
        print(f"{line_number}: {line}", end="")

    # a adds content without removing existing notes.
    additional_notes = [
        "Learn one new Python feature",
        "Organize the notes folder",
    ]
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write("\n".join(additional_notes) + "\n")
    print(f"\nAppended {len(additional_notes)} additional notes.")

    # Reopen with r and display the updated contents.
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        updated_contents = file.read()
    print("\nUpdated contents:")
    print(updated_contents, end="")

    print(
        "\nwith open(...) is preferred because it closes the file automatically, "
        "even if an error occurs while the file is being used."
    )


if __name__ == "__main__":
    main()
