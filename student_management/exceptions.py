class StudentManagementError(Exception):
    """Base exception for all student management related errors."""


class StudentNotFoundError(StudentManagementError):
    """Raised when a student cannot be found by the given ID."""


class DuplicateStudentError(StudentManagementError):
    """Raised when trying to add a student whose ID already exists."""


class InvalidInputError(StudentManagementError):
    """Raised when user supplied data fails validation."""


class FileOperationError(StudentManagementError):
    """Raised when reading from / writing to the data file fails."""
