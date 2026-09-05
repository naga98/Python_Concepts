class PayrollError(Exception):
    """Base exception for payroll errors."""


class InvalidInputError(PayrollError):
    """Raised when user input is invalid."""


class InvalidSalaryError(PayrollError):
    """Raised when salary or bonus data is invalid."""


class EmployeeNotFoundError(PayrollError):
    """Raised when an employee ID does not exist."""


class DuplicateEmployeeError(PayrollError):
    """Raised when an employee ID already exists."""


class FileOperationError(PayrollError):
    """Raised when payroll data cannot be read or written."""