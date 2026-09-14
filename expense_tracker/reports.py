import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

from .logger import get_logger


def monthly_summary(expenses, month):
    return sum((expense.amount for expense in expenses if expense.date.startswith(month)), Decimal("0.00"))


def category_summary(expenses):
    totals = defaultdict(lambda: Decimal("0.00"))
    for expense in expenses:
        totals[expense.category] += expense.amount
    return dict(sorted(totals.items()))


def highest_expense(expenses):
    return max(expenses, key=lambda expense: expense.amount, default=None)


def export_report(expenses, output_file):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=("expense_id", "date", "category", "description", "amount"))
        writer.writeheader()
        writer.writerows(expense.to_row() for expense in expenses)
    get_logger().info("Exported report to %s", output_path)
    return output_path


def generate_monthly_report(expenses, report_dir):
    report_path = Path(report_dir) / "monthly_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    months = sorted({expense.date[:7] for expense in expenses})
    with report_path.open("w", encoding="utf-8") as file:
        for month in months:
            file.write(f"{month}: ${monthly_summary(expenses, month):.2f}\n")
    return report_path