from decimal import Decimal, InvalidOperation

from .exceptions import InvalidInputError, InvalidSalaryError


def validate_text(value, field_name):
    text = str(value).strip()
    if not text:
        raise InvalidInputError(f"{field_name} cannot be empty.")
    return text


def validate_salary(value):
    try:
        salary = Decimal(str(value)).quantize(Decimal("0.01"))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise InvalidSalaryError("Salary must be a valid number.") from exc
    if salary <= 0:
        raise InvalidSalaryError("Salary must be greater than zero.")
    return salary


def validate_rate(value):
    try:
        rate = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise InvalidInputError("Tax and bonus rates must be valid numbers.") from exc
    if rate < 0 or rate > 100:
        raise InvalidInputError("Rates must be between 0 and 100.")
    return rate