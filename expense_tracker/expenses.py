import csv
import uuid
from dataclasses import asdict, dataclass
from decimal import Decimal
from pathlib import Path

from .exceptions import ExpenseNotFoundError, FileOperationError
from .logger import get_logger
from .validation import validate_amount, validate_date, validate_text

CSV_FIELDS = ("expense_id", "date", "category", "description", "amount")


@dataclass
class Expense:
    expense_id: str
    date: str
    category: str
    description: str
    amount: Decimal

    def to_row(self):
        row = asdict(self)
        row["amount"] = f"{self.amount:.2f}"
        return row


class ExpenseManager:
    def __init__(self, csv_file="expenses.csv", log_file="expense_tracker.log", report_dir="monthly_reports"):
        self.csv_file = Path(csv_file)
        self.report_dir = Path(report_dir)
        self.logger = get_logger(log_file)
        self.expenses = self._load()

    def _load(self):
        if not self.csv_file.exists():
            return []
        try:
            with self.csv_file.open(newline="", encoding="utf-8") as file:
                return [
                    Expense(row["expense_id"], row["date"], row["category"], row["description"], Decimal(row["amount"]))
                    for row in csv.DictReader(file)
                ]
        except (OSError, KeyError, ValueError) as exc:
            raise FileOperationError(f"Could not load expenses: {exc}") from exc

    def _save(self):
        try:
            self.csv_file.parent.mkdir(parents=True, exist_ok=True)
            with self.csv_file.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
                writer.writeheader()
                writer.writerows(expense.to_row() for expense in self.expenses)
        except OSError as exc:
            raise FileOperationError(f"Could not save expenses: {exc}") from exc

    def _refresh_report(self):
        from .reports import generate_monthly_report

        generate_monthly_report(self.expenses, self.report_dir)

    def add_expense(self, date, category, description, amount):
        expense = Expense(str(uuid.uuid4()), validate_date(date), validate_text(category, "Category"), validate_text(description, "Description"), validate_amount(amount))
        self.expenses.append(expense)
        self._save()
        self._refresh_report()
        self.logger.info("Added expense %s", expense.expense_id)
        return expense

    def _find(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        raise ExpenseNotFoundError(f"Expense not found: {expense_id}")

    def delete_expense(self, expense_id):
        expense = self._find(expense_id)
        self.expenses.remove(expense)
        self._save()
        self._refresh_report()
        self.logger.info("Deleted expense %s", expense_id)

    def update_expense(self, expense_id, **changes):
        expense = self._find(expense_id)
        if "date" in changes:
            expense.date = validate_date(changes["date"])
        if "category" in changes:
            expense.category = validate_text(changes["category"], "Category")
        if "description" in changes:
            expense.description = validate_text(changes["description"], "Description")
        if "amount" in changes:
            expense.amount = validate_amount(changes["amount"])
        self._save()
        self._refresh_report()
        self.logger.info("Updated expense %s", expense_id)
        return expense