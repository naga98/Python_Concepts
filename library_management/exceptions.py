class LibraryError(Exception):
    """Base exception for library errors."""


class BookNotFoundError(LibraryError):
    """Raised when a book ID does not exist."""


class AlreadyBorrowedError(LibraryError):
    """Raised when an unavailable book is borrowed."""


class InvalidBookIDError(LibraryError):
    """Raised when a book ID is empty or invalid."""


class FileOperationError(LibraryError):
    """Raised when library data cannot be read or written."""