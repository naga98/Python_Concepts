import csv
from io import StringIO
from pathlib import Path

import pandas as pd

pd.set_option("display.width", 140)

BASE_DIR = Path(__file__).parent
TXT_PATH = BASE_DIR / "sales.txt"
OUTPUT_PATH = BASE_DIR / "output" / "sales_report.csv"

HEADER = "order_id,product,quantity,price,city"
RECORDS = [
    "101,Laptop,1,65000,Bangalore",
    "102,Mouse,2,1200,Delhi",
    "103,Keyboard,3,2500,Mumbai",
    "104,Monitor,2,14000,Pune",
    "105,Laptop,1,72000,Hyderabad",
    "106,Headphones,4,3500,Delhi",
    "107,Mobile,1,45000,Chennai",
    "108,Mouse,5,900,Bangalore",
    "109,Tablet,2,28000,Mumbai",
    "110,Laptop,2,58000,Delhi",
    "111,Monitor,1,19000,Kolkata",
    "112,Keyboard,2,1800,Chennai",
    "113,Headphones,1,12000,Bangalore",
    "114,Mobile,3,22000,Pune",
    "115,Tablet,1,35000,Delhi",
    "116,Laptop,1,89000,Mumbai",
    "117,Mouse,3,1500,Hyderabad",
    "118,Monitor,2,11000,Bangalore",
    "119,Mobile,2,31000,Kolkata",
    "120,Keyboard,4,2200,Delhi",
    "121,Headphones,2,6500,Chennai",
    "122,Tablet,1,42000,Bangalore",
    "123,Laptop,3,54000,Pune",
    "124,Mouse,10,750,Mumbai",
    "125,Monitor,1,27000,Delhi",
    "126,Mobile,1,68000,Hyderabad",
    "127,Headphones,6,2100,Kolkata",
    "128,Keyboard,1,9500,Bangalore",
    "129,Tablet,2,19500,Chennai",
    "130,Laptop,1,47000,Delhi",
    "131,Mobile,4,16000,Mumbai",
    "132,Monitor,3,8900,Pune",
]


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# 1. Create / write the text file using normal Python file handling
with open(TXT_PATH, "w", encoding="utf-8") as f:
    f.write(HEADER + "\n")
    for line in RECORDS:
        f.write(line + "\n")
print(f"Written {len(RECORDS)} transactions to {TXT_PATH}")

# 2. Read it back using normal Python file handling
section("2. Reading sales.txt with plain Python file handling")
with open(TXT_PATH, "r", encoding="utf-8") as f:
    raw_lines = [line.strip() for line in f if line.strip()]

print("Total lines (incl. header):", len(raw_lines))
print("First 5 lines:")
for line in raw_lines[:5]:
    print("  ", line)

section("3. Parsing the raw lines manually with csv.reader")
reader = csv.reader(StringIO("\n".join(raw_lines)))
header = next(reader)
manual_rows = list(reader)
print("Header :", header)
print("Rows   :", len(manual_rows))
print("Sample :", manual_rows[0])

# 4. Load the same data using Pandas -> DataFrame
section("4. Loading the same file with Pandas into a DataFrame")
df = pd.read_csv(TXT_PATH)
print(df.head())
print("\nType:", type(df))
print("Shape:", df.shape)

section("5. info()")
df.info()

# 6. revenue = quantity * price
df["revenue"] = df["quantity"] * df["price"]

section("6. Revenue per order")
print(df.head(10))

section("7. Total revenue")
print(f"Rs. {df['revenue'].sum():,}")

section("8. Average order value")
print(f"Rs. {df['revenue'].mean():,.2f}")

section("9. Highest-value order")
print(df.loc[df["revenue"].idxmax()])

section("10. Lowest-value order")
print(df.loc[df["revenue"].idxmin()])

section("11. Revenue product-wise")
print(df.groupby("product")["revenue"].sum().sort_values(ascending=False))

section("12. Revenue city-wise")
print(df.groupby("city")["revenue"].sum().sort_values(ascending=False))

# 13. Save processed data
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)
print(f"\nProcessed data saved to: {OUTPUT_PATH}")
