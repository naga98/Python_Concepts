# Parent Class
class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def display_balance(self):
        print("Current Balance:", self.balance)

    def account_details(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


# Child Class - Savings Account
class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance,
        interest_rate
    ):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def savings_details(self):
        print("Interest Rate:", self.interest_rate, "%")


# Child Class - Current Account
class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance,
        overdraft_limit
    ):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def current_details(self):
        print("Overdraft Limit:", self.overdraft_limit)


# Child Class - Salary Account
class SalaryAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance,
        employer,
        monthly_salary
    ):
        super().__init__(account_number, holder_name, balance)
        self.employer = employer
        self.monthly_salary = monthly_salary

    def salary_details(self):
        print("Employer:", self.employer)
        print("Monthly Salary:", self.monthly_salary)


# Creating Savings Account objects
savings1 = SavingsAccount(
    "SA1001",
    "Rahul",
    50000,
    6.5
)

savings2 = SavingsAccount(
    "SA1002",
    "Priya",
    75000,
    7.0
)


# Creating Current Account objects
current1 = CurrentAccount(
    "CA2001",
    "Arun",
    100000,
    25000
)

current2 = CurrentAccount(
    "CA2002",
    "Sneha",
    150000,
    50000
)


# Creating Salary Account objects
salary1 = SalaryAccount(
    "SAL3001",
    "Kiran",
    60000,
    "Infosys",
    90000
)

salary2 = SalaryAccount(
    "SAL3002",
    "Anjali",
    80000,
    "TCS",
    100000
)


# Savings Account demonstration
print("========== Savings Account 1 ==========")

savings1.account_details()
savings1.savings_details()

savings1.deposit(5000)
savings1.display_balance()


# Savings Account 2
print("\n========== Savings Account 2 ==========")

savings2.account_details()
savings2.savings_details()

savings2.deposit(10000)
savings2.display_balance()


# Current Account demonstration
print("\n========== Current Account 1 ==========")

current1.account_details()
current1.current_details()

current1.deposit(20000)
current1.display_balance()


# Current Account 2
print("\n========== Current Account 2 ==========")

current2.account_details()
current2.current_details()

current2.deposit(30000)
current2.display_balance()


# Salary Account demonstration
print("\n========== Salary Account 1 ==========")

salary1.account_details()
salary1.salary_details()

salary1.deposit(15000)
salary1.display_balance()


# Salary Account 2
print("\n========== Salary Account 2 ==========")

salary2.account_details()
salary2.salary_details()

salary2.deposit(20000)
salary2.display_balance()