from datetime import date

try:
    from .expenses import ExpenseManager
    from .reports import category_summary, export_report, highest_expense, monthly_summary
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from expense_tracker.expenses import ExpenseManager
    from expense_tracker.reports import category_summary, export_report, highest_expense, monthly_summary


def main():
    manager = ExpenseManager()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add expense")
        print("2. Delete expense")
        print("3. Update expense")
        print("4. View summary")
        print("5. Export report")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                expense = manager.add_expense(
                    input("Date (YYYY-MM-DD): "),
                    input("Category: "),
                    input("Description: "),
                    input("Amount: "),
                )
                print(f"Added expense with ID: {expense.expense_id}")
            elif choice == "2":
                manager.delete_expense(input("Expense ID: ").strip())
                print("Expense deleted.")
            elif choice == "3":
                expense_id = input("Expense ID: ").strip()
                manager.update_expense(
                    expense_id,
                    date=input("New date (YYYY-MM-DD): "),
                    category=input("New category: "),
                    description=input("New description: "),
                    amount=input("New amount: "),
                )
                print("Expense updated.")
            elif choice == "4":
                month = date.today().strftime("%Y-%m")
                print(f"Loaded {len(manager.expenses)} expense(s).")
                print(f"This month's total: ${monthly_summary(manager.expenses, month):.2f}")
                print("Category totals:", category_summary(manager.expenses))
                largest = highest_expense(manager.expenses)
                print(f"Highest expense: {largest.description} (${largest.amount:.2f})" if largest else "Highest expense: none")
            elif choice == "5":
                export_report(manager.expenses, "expense_report.csv")
                print("Report exported to expense_report.csv.")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 6.")
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()