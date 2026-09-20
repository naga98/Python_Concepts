# Level 1 - Parent Class
class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)


# Level 2 - Employee inherits Person
class Employee(Person):

    def __init__(self, name, age, city, employee_id, salary, company):
        super().__init__(name, age, city)

        self.employee_id = employee_id
        self.salary = salary
        self.company = company

    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Company:", self.company)


# Level 3 - Developer inherits Employee
class Developer(Employee):

    def __init__(
        self,
        name,
        age,
        city,
        employee_id,
        salary,
        company,
        language,
        framework,
        experience
    ):
        super().__init__(
            name,
            age,
            city,
            employee_id,
            salary,
            company
        )

        self.language = language
        self.framework = framework
        self.experience = experience

    def display_developer(self):
        print("Programming Language:", self.language)
        print("Framework:", self.framework)
        print("Experience:", self.experience, "years")


# Creating 5 Developer objects

developer1 = Developer(
    "Rahul", 25, "Bengaluru",
    101, 70000, "TechCorp",
    "Python", "Django", 3
)

developer2 = Developer(
    "Priya", 27, "Hyderabad",
    102, 80000, "TechCorp",
    "Java", "Spring Boot", 5
)

developer3 = Developer(
    "Arun", 24, "Chennai",
    103, 65000, "TechCorp",
    "JavaScript", "React", 2
)

developer4 = Developer(
    "Sneha", 29, "Pune",
    104, 95000, "TechCorp",
    "Python", "FastAPI", 6
)

developer5 = Developer(
    "Kiran", 26, "Mumbai",
    105, 75000, "TechCorp",
    "Java", "Spring", 4
)


# Demonstrating Developer 1
print("========== Developer 1 ==========")

# Method from Person
developer1.display_person()

# Method from Employee
developer1.display_employee()

# Method from Developer
developer1.display_developer()


# Demonstrating Developer 2
print("\n========== Developer 2 ==========")
developer2.display_person()
developer2.display_employee()
developer2.display_developer()


# Demonstrating Developer 3
print("\n========== Developer 3 ==========")
developer3.display_person()
developer3.display_employee()
developer3.display_developer()


# Demonstrating Developer 4
print("\n========== Developer 4 ==========")
developer4.display_person()
developer4.display_employee()
developer4.display_developer()


# Demonstrating Developer 5
print("\n========== Developer 5 ==========")
developer5.display_person()
developer5.display_employee()
developer5.display_developer()