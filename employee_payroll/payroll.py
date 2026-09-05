import csv
import uuid
from dataclasses import asdict, dataclass
from decimal import Decimal
from pathlib import Path

from .exceptions import DuplicateEmployeeError, EmployeeNotFoundError, FileOperationError
from .logger import get_error_logger, get_payroll_logger
from .reports import format_payslip, save_payslip
from .validation import validate_rate, validate_salary, validate_text

EMPLOYEE_FIELDS = ("employee_id", "name", "department", "salary")
RECORD_FIELDS = ("employee_id", "name", "base_salary", "bonus", "gross_salary", "tax", "net_salary")


@dataclass
class Employee:
    employee_id: str
    name: str
    department: str
    salary: Decimal

    def to_row(self):
        row = asdict(self)
        row["salary"] = f"{self.salary:.2f}"
        return row


class Payroll:
    def __init__(self, employees_file="employees.csv", records_file="payroll_records.csv", payroll_log="payroll.log", error_log="error.log", payslip_dir="payslips"):
        self.employees_file = Path(employees_file)
        self.records_file = Path(records_file)
        self.payslip_dir = Path(payslip_dir)
        self.payroll_logger = get_payroll_logger(payroll_log)
        self.error_logger = get_error_logger(error_log)
        self.employees = self._load_employees()

    def _load_employees(self):
        if not self.employees_file.exists():
            return []
        try:
            with self.employees_file.open(newline="", encoding="utf-8") as file:
                return [Employee(row["employee_id"], row["name"], row["department"], Decimal(row["salary"])) for row in csv.DictReader(file)]
        except (OSError, KeyError, ValueError) as exc:
            self.error_logger.error("Could not load employees: %s", exc)
            raise FileOperationError(f"Could not load employees: {exc}") from exc

    def _save_employees(self):
        try:
            self.employees_file.parent.mkdir(parents=True, exist_ok=True)
            with self.employees_file.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=EMPLOYEE_FIELDS)
                writer.writeheader()
                writer.writerows(employee.to_row() for employee in self.employees)
        except OSError as exc:
            self.error_logger.error("Could not save employees: %s", exc)
            raise FileOperationError(f"Could not save employees: {exc}") from exc

    def add_employee(self, name, department, salary, employee_id=None):
        name = validate_text(name, "Name")
        department = validate_text(department, "Department")
        salary = validate_salary(salary)
        employee_id = validate_text(employee_id or str(uuid.uuid4()), "Employee ID")
        if any(employee.employee_id == employee_id for employee in self.employees):
            raise DuplicateEmployeeError(f"Employee ID already exists: {employee_id}")
        employee = Employee(employee_id, name, department, salary)
        self.employees.append(employee)
        self._save_employees()
        self.payroll_logger.info("Added employee %s", employee_id)
        return employee

    def _find_employee(self, employee_id):
        employee_id = validate_text(employee_id, "Employee ID")
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        raise EmployeeNotFoundError(f"Employee not found: {employee_id}")

    def calculate_bonus(self, employee_id, bonus_rate):
        employee = self._find_employee(employee_id)
        rate = validate_rate(bonus_rate)
        return (employee.salary * rate / Decimal("100")).quantize(Decimal("0.01"))

    def calculate_tax(self, gross_salary, tax_rate=10):
        salary = validate_salary(gross_salary)
        rate = validate_rate(tax_rate)
        return (salary * rate / Decimal("100")).quantize(Decimal("0.01"))

    def calculate_salary(self, employee_id, bonus_rate=0, tax_rate=10):
        employee = self._find_employee(employee_id)
        bonus = self.calculate_bonus(employee_id, bonus_rate)
        gross_salary = employee.salary + bonus
        tax = self.calculate_tax(gross_salary, tax_rate)
        net_salary = gross_salary - tax
        return {"employee": employee, "bonus": bonus, "gross_salary": gross_salary, "tax": tax, "net_salary": net_salary}

    def generate_payslip(self, employee_id, bonus_rate=0, tax_rate=10):
        result = self.calculate_salary(employee_id, bonus_rate, tax_rate)
        employee = result["employee"]
        content = format_payslip(employee, result["gross_salary"], result["bonus"], result["tax"], result["net_salary"])
        path = save_payslip(content, self.payslip_dir, employee.employee_id)
        try:
            self.records_file.parent.mkdir(parents=True, exist_ok=True)
            exists = self.records_file.exists()
            with self.records_file.open("a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=RECORD_FIELDS)
                if not exists:
                    writer.writeheader()
                writer.writerow({"employee_id": employee.employee_id, "name": employee.name, "base_salary": f"{employee.salary:.2f}", "bonus": f"{result['bonus']:.2f}", "gross_salary": f"{result['gross_salary']:.2f}", "tax": f"{result['tax']:.2f}", "net_salary": f"{result['net_salary']:.2f}"})
        except OSError as exc:
            self.error_logger.error("Could not save payroll record: %s", exc)
            raise FileOperationError(f"Could not save payroll record: {exc}") from exc
        self.payroll_logger.info("Generated salary and payslip for %s", employee.employee_id)
        return path, result