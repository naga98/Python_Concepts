from decimal import Decimal
from pathlib import Path


def format_payslip(employee, gross_salary, bonus, tax, net_salary):
    return (
        "EMPLOYEE PAYSLIP\n"
        f"Employee ID: {employee.employee_id}\n"
        f"Name: {employee.name}\n"
        f"Department: {employee.department}\n"
        f"Base salary: ${employee.salary:.2f}\n"
        f"Bonus: ${bonus:.2f}\n"
        f"Gross salary: ${gross_salary:.2f}\n"
        f"Tax: ${tax:.2f}\n"
        f"Net salary: ${net_salary:.2f}\n"
    )


def save_payslip(content, output_dir, employee_id):
    output_path = Path(output_dir) / f"payslip_{employee_id}.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path