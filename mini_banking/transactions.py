import csv
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

from .exceptions import FileOperationError
from .utilities import timestamp

TRANSACTION_FIELDS = ("timestamp", "transaction_type", "from_account", "to_account", "amount")


@dataclass
class Transaction:
    transaction_type: str
    from_account: str
    to_account: str
    amount: Decimal

    def to_row(self):
        return {"timestamp": timestamp(), "transaction_type": self.transaction_type, "from_account": self.from_account, "to_account": self.to_account, "amount": f"{self.amount:.2f}"}


class TransactionStore:
    def __init__(self, history_file="transactions.csv"):
        self.history_file = Path(history_file)

    def record(self, transaction):
        try:
            self.history_file.parent.mkdir(parents=True, exist_ok=True)
            exists = self.history_file.exists()
            with self.history_file.open("a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=TRANSACTION_FIELDS)
                if not exists:
                    writer.writeheader()
                writer.writerow(transaction.to_row())
        except OSError as exc:
            raise FileOperationError(f"Could not save transaction: {exc}") from exc

    def history(self):
        if not self.history_file.exists():
            return []
        try:
            with self.history_file.open(newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except OSError as exc:
            raise FileOperationError(f"Could not read transaction history: {exc}") from exc


def generate_report(history, output_file="transaction_report.txt"):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        file.write("TRANSACTION REPORT\n==================\n")
        for item in history:
            file.write(f"{item['timestamp']} | {item['transaction_type']} | ${item['amount']} | {item['from_account']} -> {item['to_account']}\n")
    return output_path