class BankingError(Exception):
    """Base exception for banking errors."""


class AccountNotFoundError(BankingError):
    """Raised when an account cannot be found."""


class DuplicateAccountError(BankingError):
    """Raised when an account ID already exists."""


class InsufficientBalanceError(BankingError):
    """Raised when an account lacks funds."""


class InvalidAmountError(BankingError):
    """Raised when an amount is invalid."""


class InvalidInputError(BankingError):
    """Raised when required input is missing."""


class FileOperationError(BankingError):
    """Raised when banking data cannot be read or written."""