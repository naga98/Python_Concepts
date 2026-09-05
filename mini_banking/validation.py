from decimal import Decimal, InvalidOperation

from .exceptions import InvalidAmountError, InvalidInputError


def validate_text(value, field_name):
    text = str(value).strip()
    if not text:
        raise InvalidInputError(f"{field_name} cannot be empty.")
    return text


def validate_amount(value):
    try:
        amount = Decimal(str(value)).quantize(Decimal("0.01"))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise InvalidAmountError("Amount must be a valid number.") from exc
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero.")
    return amount