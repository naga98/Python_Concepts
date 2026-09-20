"""Generates a deliberately messy customer dataset (messy_customers.csv)."""

import random
from pathlib import Path

OUT_PATH = Path(__file__).parent / "messy_customers.csv"

random.seed(42)

FIRST = ["aarav", "isha", "rohan", "sneha", "karan", "ananya", "vivek", "priya",
         "arjun", "meera", "siddharth", "nisha", "aditya", "kavya", "rahul",
         "pooja", "manish", "divya", "nikhil", "ritika", "harsh", "tanvi",
         "yash", "sanya", "imran", "lakshmi", "devendra", "shreya", "amit", "neha"]
LAST = ["sharma", "patel", "mehta", "iyer", "singh", "rao", "nair", "desai",
        "reddy", "joshi", "bose", "verma", "kulkarni", "menon", "yadav"]
CITIES = ["mumbai", "DELHI", "Bangalore", "  chennai", "pune  ", "HYDERABAD",
          "kolkata", "Jaipur", "  AHMEDABAD  ", "surat"]


def messy_case(text):
    style = random.choice(["lower", "upper", "title", "mixed", "spaced"])
    if style == "lower":
        return text.lower()
    if style == "upper":
        return text.upper()
    if style == "title":
        return text.title()
    if style == "mixed":
        return "".join(c.upper() if i % 2 else c.lower() for i, c in enumerate(text))
    return f"   {text.title()}   "


rows = []
for i in range(1, 106):
    name = messy_case(f"{random.choice(FIRST)} {random.choice(LAST)}")
    city = random.choice(CITIES)

    # age: sometimes blank, sometimes 'NA', sometimes a float-looking string
    r = random.random()
    if r < 0.08:
        age = ""
    elif r < 0.12:
        age = "NA"
    elif r < 0.18:
        age = f"{random.randint(18, 60)}.0"
    else:
        age = str(random.randint(18, 60))

    email = f"{name.strip().lower().replace(' ', '.')}@example.com"
    if random.random() < 0.07:
        email = ""
    elif random.random() < 0.2:
        email = f"  {email.upper()}  "

    # purchase_amount: sometimes blank, sometimes with currency symbol/commas
    r = random.random()
    if r < 0.09:
        amount = ""
    elif r < 0.2:
        amount = f"Rs. {random.randint(1000, 90000):,}"
    else:
        amount = str(random.randint(500, 95000))

    rating = "" if random.random() < 0.1 else f"{random.uniform(1, 5):.1f}"

    rows.append([f"C{i:03d}", name, age, city, email, amount, rating])

# inject duplicate rows
for idx in random.sample(range(len(rows)), 12):
    rows.append(list(rows[idx]))

random.shuffle(rows)

with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
    f.write("customer_id,name,age,city,email,purchase_amount,rating\n")
    for row in rows:
        f.write(",".join(f'"{v}"' for v in row) + "\n")

print(f"Created {OUT_PATH} with {len(rows)} rows (including duplicates).")
