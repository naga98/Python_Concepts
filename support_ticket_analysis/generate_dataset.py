"""Generate a sample support tickets dataset (tickets.csv)."""
import csv
import random

random.seed(42)

CATEGORIES = ["Payment", "Technical", "Login", "Course", "Refund", "Account"]
PRIORITIES = ["Low", "Medium", "High", "Critical"]
STATUSES = ["Open", "In Progress", "Resolved", "Closed"]
AGENTS = ["Alice", "Bob", "Carol", "David", "Emma"]

FIRST_NAMES = ["John", "Mary", "James", "Patricia", "Robert", "Linda", "Michael",
               "Barbara", "William", "Elizabeth", "David", "Susan", "Richard",
               "Jessica", "Joseph", "Sarah", "Thomas", "Karen", "Charles", "Nancy"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
              "Davis", "Rodriguez", "Martinez", "Wilson", "Anderson", "Taylor",
              "Thomas", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson"]

TOTAL_TICKETS = 60

rows = []
for i in range(1, TOTAL_TICKETS + 1):
    ticket_id = f"T{i:03d}"
    customer_name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    category = random.choice(CATEGORIES)
    priority = random.choice(PRIORITIES)
    status = random.choice(STATUSES)
    assigned_agent = random.choice(AGENTS)
    resolution_time = random.randint(1, 72)  # hours

    rows.append([ticket_id, customer_name, category, priority, status,
                 assigned_agent, resolution_time])

with open("tickets.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ticket_id", "customer_name", "category", "priority",
                      "status", "assigned_agent", "resolution_time"])
    writer.writerows(rows)

print(f"Generated {TOTAL_TICKETS} tickets into tickets.csv")
