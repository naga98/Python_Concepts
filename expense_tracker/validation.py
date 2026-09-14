from datetime import date
from decimal import Decimal, InvalidOperation

from .exceptions import InvalidInputError


def validate_date(value):
    if isinstance(value, date):
        return value.isoformat()
    try:
        return date.fromisoformat(str(value)).isoformat()
    except (TypeError, ValueError) as exc:
        raise InvalidInputError("Date must use YYYY-MM-DD format.") from exc


def validate_text(value, field_name):
    text = str(value).strip()
    if not text:
        raise InvalidInputError(f"{field_name} cannot be empty.")
    return text


def validate_amount(value):
    try:
        amount = Decimal(str(value)).quantize(Decimal("0.01"))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise InvalidInputError("Amount must be a positive number.") from exc
    if amount <= 0:
        raise InvalidInputError("Amount must be greater than zero.")
    return amount