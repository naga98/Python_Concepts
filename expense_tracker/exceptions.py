class ExpenseTrackerError(Exception):
    """Base exception for expense tracker errors."""


class InvalidInputError(ExpenseTrackerError):
    """Raised when expense data is invalid."""


class ExpenseNotFoundError(ExpenseTrackerError):
    """Raised when an expense ID does not exist."""


class FileOperationError(ExpenseTrackerError):
    """Raised when expense data cannot be read or written."""