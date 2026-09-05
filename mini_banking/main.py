try:
    from .customers import Bank
    from .transactions import generate_report
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from mini_banking.customers import Bank
    from mini_banking.transactions import generate_report


def main():
    bank = Bank()
    while True:
        print("\nMini Banking System")
        print("1. Create account\n2. Deposit\n3. Withdraw\n4. Transfer money\n5. Check balance\n6. Transaction history\n7. Generate report\n8. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                account = bank.create_account(input("Customer name: "))
                print(f"Account created. ID: {account.account_id}")
            elif choice == "2":
                print(f"New balance: ${bank.deposit(input('Account ID: '), input('Amount: ')):.2f}")
            elif choice == "3":
                print(f"New balance: ${bank.withdraw(input('Account ID: '), input('Amount: ')):.2f}")
            elif choice == "4":
                bank.transfer(input("From account: "), input("To account: "), input("Amount: "))
                print("Transfer complete.")
            elif choice == "5":
                print(f"Balance: ${bank.check_balance(input('Account ID: ')):.2f}")
            elif choice == "6":
                for item in bank.transaction_history():
                    print(item)
            elif choice == "7":
                path = generate_report(bank.transaction_history())
                print(f"Report saved to {path}")
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 8.")
        except Exception as error:
            bank.logger.error("Transaction failed: %s", error)
            print(f"Error: {error}")


if __name__ == "__main__":
    main()