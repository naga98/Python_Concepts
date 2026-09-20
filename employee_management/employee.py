# Parent Class
class Employee:

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

    def calculate_salary(self):
        return self.salary


# Child Class - Developer
class Developer(Employee):

    def __init__(self, employee_id, name, salary, department, programming_language):
        super().__init__(employee_id, name, salary, department)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print("Programming Language:", self.programming_language)


# Child Class - Manager
class Manager(Employee):

    def __init__(self, employee_id, name, salary, department, team_size):
        super().__init__(employee_id, name, salary, department)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print("Team Size:", self.team_size)


# Child Class - HR
class HR(Employee):

    def __init__(self, employee_id, name, salary, department, region):
        super().__init__(employee_id, name, salary, department)
        self.region = region

    def display_details(self):
        super().display_details()
        print("Region:", self.region)


# Creating 2 Developer objects
developer1 = Developer(
    101, "Rahul", 80000, "IT", "Python"
)

developer2 = Developer(
    102, "Priya", 85000, "IT", "Java"
)


# Creating 2 Manager objects
manager1 = Manager(
    201, "Arun", 120000, "Management", 10
)

manager2 = Manager(
    202, "Sneha", 130000, "Management", 15
)


# Creating 2 HR objects
hr1 = HR(
    301, "Kiran", 70000, "HR", "South India"
)

hr2 = HR(
    302, "Anjali", 75000, "HR", "North India"
)


# Display Developer details
print("----- Developer 1 -----")
developer1.display_details()
print("Calculated Salary:", developer1.calculate_salary())

print("\n----- Developer 2 -----")
developer2.display_details()
print("Calculated Salary:", developer2.calculate_salary())


# Display Manager details
print("\n----- Manager 1 -----")
manager1.display_details()
print("Calculated Salary:", manager1.calculate_salary())

print("\n----- Manager 2 -----")
manager2.display_details()
print("Calculated Salary:", manager2.calculate_salary())


# Display HR details
print("\n----- HR 1 -----")
hr1.display_details()
print("Calculated Salary:", hr1.calculate_salary())

print("\n----- HR 2 -----")
hr2.display_details()
print("Calculated Salary:", hr2.calculate_salary())