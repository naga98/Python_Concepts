try:
    from .books import Library
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from library_management.books import Library


def display_books(books):
    if not books:
        print("No books found.")
        return
    for book in books:
        status = "Borrowed" if book.borrowed else "Available"
        print(f"{book.book_id} | {book.title} | {book.author} | {status}")


def main():
    library = Library()
    actions = {
        "1": lambda: print(f"Added book: {library.add_book(input('Title: '), input('Author: ')).book_id}"),
        "2": lambda: print(f"Borrowed: {library.borrow_book(input('Book ID: '), input('Borrower: ')).title}"),
        "3": lambda: print(f"Returned: {library.return_book(input('Book ID: '), input('Borrower: ')).title}"),
        "4": lambda: display_books(library.search_books(input("Search title or author: "))),
        "5": lambda: display_books(library.available_books()),
        "6": lambda: display_books(library.books),
        "7": lambda: print(library.borrowing_history()),
    }
    while True:
        print("\nLibrary Management System")
        print("1. Add book\n2. Borrow book\n3. Return book\n4. Search book\n5. View available books\n6. View all books\n7. View borrowing history\n8. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "8":
            print("Goodbye!")
            break
        try:
            actions[choice]()
        except KeyError:
            print("Please choose a number from 1 to 8.")
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()