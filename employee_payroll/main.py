try:
    from .payroll import Payroll
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from employee_payroll.payroll import Payroll


def main():
    payroll = Payroll()
    while True:
        print("\nEmployee Payroll Calculator")
        print("1. Add employee\n2. Calculate salary\n3. Calculate bonus\n4. Calculate tax\n5. Generate payslip\n6. List employees\n7. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                employee = payroll.add_employee(input("Name: "), input("Department: "), input("Salary: "))
                print(f"Employee added. ID: {employee.employee_id}")
            elif choice in {"2", "5"}:
                employee_id = input("Employee ID: ")
                bonus_rate = input("Bonus rate (%): ")
                tax_rate = input("Tax rate (%): ")
                if choice == "2":
                    result = payroll.calculate_salary(employee_id, bonus_rate, tax_rate)
                    print(f"Gross: ${result['gross_salary']:.2f} | Tax: ${result['tax']:.2f} | Net: ${result['net_salary']:.2f}")
                else:
                    path, result = payroll.generate_payslip(employee_id, bonus_rate, tax_rate)
                    print(f"Payslip saved to {path} | Net salary: ${result['net_salary']:.2f}")
            elif choice == "3":
                print(f"Bonus: ${payroll.calculate_bonus(input('Employee ID: '), input('Bonus rate (%): ')):.2f}")
            elif choice == "4":
                print(f"Tax: ${payroll.calculate_tax(input('Gross salary: '), input('Tax rate (%): ')):.2f}")
            elif choice == "6":
                for employee in payroll.employees:
                    print(f"{employee.employee_id} | {employee.name} | {employee.department} | ${employee.salary:.2f}")
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 7.")
        except Exception as error:
            payroll.error_logger.error("Operation failed: %s", error)
            print(f"Error: {error}")


if __name__ == "__main__":
    main()