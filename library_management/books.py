import csv
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path

from .exceptions import AlreadyBorrowedError, BookNotFoundError, FileOperationError, InvalidBookIDError
from .logger import get_logger

BOOK_FIELDS = ("book_id", "title", "author", "borrowed")


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    borrowed: bool = False

    def to_row(self):
        row = asdict(self)
        row["borrowed"] = str(self.borrowed)
        return row


class Library:
    def __init__(self, books_file="books.csv", history_file="borrowing_history.csv", log_file="library_management.log"):
        self.books_file = Path(books_file)
        self.history_file = Path(history_file)
        self.logger = get_logger(log_file)
        self.books = self._load_books()

    def _load_books(self):
        if not self.books_file.exists():
            return []
        try:
            with self.books_file.open(newline="", encoding="utf-8") as file:
                return [Book(row["book_id"], row["title"], row["author"], row["borrowed"] == "True") for row in csv.DictReader(file)]
        except (OSError, KeyError) as exc:
            raise FileOperationError(f"Could not load books: {exc}") from exc

    def _save_books(self):
        try:
            self.books_file.parent.mkdir(parents=True, exist_ok=True)
            with self.books_file.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=BOOK_FIELDS)
                writer.writeheader()
                writer.writerows(book.to_row() for book in self.books)
        except OSError as exc:
            raise FileOperationError(f"Could not save books: {exc}") from exc

    def _validate_book_id(self, book_id):
        if not isinstance(book_id, str) or not book_id.strip():
            raise InvalidBookIDError("Book ID cannot be empty.")
        return book_id.strip()

    def _find_book(self, book_id):
        book_id = self._validate_book_id(book_id)
        for book in self.books:
            if book.book_id == book_id:
                return book
        raise BookNotFoundError(f"Book not found: {book_id}")

    def add_book(self, title, author):
        if not str(title).strip() or not str(author).strip():
            raise ValueError("Title and author are required.")
        book = Book(str(uuid.uuid4()), str(title).strip(), str(author).strip())
        self.books.append(book)
        self._save_books()
        self.logger.info("Added book %s", book.book_id)
        return book

    def borrow_book(self, book_id, borrower):
        book = self._find_book(book_id)
        borrower = str(borrower).strip()
        if not borrower:
            raise ValueError("Borrower name is required.")
        if book.borrowed:
            raise AlreadyBorrowedError(f"Book is already borrowed: {book.book_id}")
        book.borrowed = True
        self._save_books()
        self._save_history("BORROW", book, borrower)
        self.logger.info("Borrowed book %s by %s", book.book_id, borrower)
        return book

    def return_book(self, book_id, borrower=""):
        book = self._find_book(book_id)
        if not book.borrowed:
            raise ValueError(f"Book is not currently borrowed: {book.book_id}")
        book.borrowed = False
        self._save_books()
        self._save_history("RETURN", book, str(borrower).strip())
        self.logger.info("Returned book %s by %s", book.book_id, borrower)
        return book

    def search_books(self, query):
        query = str(query).strip().lower()
        return [book for book in self.books if query in book.title.lower() or query in book.author.lower()]

    def available_books(self):
        return [book for book in self.books if not book.borrowed]

    def borrowing_history(self):
        if not self.history_file.exists():
            return []
        try:
            with self.history_file.open(newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except OSError as exc:
            raise FileOperationError(f"Could not load history: {exc}") from exc

    def _save_history(self, action, book, borrower):
        fields = ("action", "book_id", "title", "borrower")
        try:
            self.history_file.parent.mkdir(parents=True, exist_ok=True)
            history = self.borrowing_history()
            history.append({"action": action, "book_id": book.book_id, "title": book.title, "borrower": borrower})
            with self.history_file.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(history)
        except (OSError, ValueError) as exc:
            raise FileOperationError(f"Could not save borrowing history: {exc}") from exc