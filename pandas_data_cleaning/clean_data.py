"""Pandas Data Cleaning Challenge - clean a messy customer dataset."""

from pathlib import Path

import pandas as pd

pd.set_option("display.width", 160)
pd.set_option("display.max_columns", 20)

BASE_DIR = Path(__file__).parent
RAW_PATH = BASE_DIR / "messy_customers.csv"
OUTPUT_PATH = BASE_DIR / "output" / "cleaned_customer_data.csv"


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# Treat these placeholder strings as missing while reading
df = pd.read_csv(RAW_PATH, na_values=["", " ", "NA", "na", "n/a", "null", "-"],
                 skipinitialspace=False)

shape_before = df.shape

section("A. DIRTY DATASET - BEFORE CLEANING")
print(df.head(15))
print("\nShape:", shape_before)
print("\nData types (note everything is object/string):")
print(df.dtypes)

section("B. info() on dirty data")
df.info()

# ---------------------------------------------------------------- MISSING DATA
section("1. Detect missing data - isnull()")
print(df.isnull().head(15))

section("2. Count missing values - isnull().sum()")
print(df.isnull().sum())
print("\nTotal missing cells:", int(df.isnull().sum().sum()))

section("3. Rows that contain at least one missing value")
print(df[df.isnull().any(axis=1)].head(10))

# ------------------------------------------------------------------ DUPLICATES
section("4. Detect duplicates - duplicated()")
print("Duplicate rows found:", int(df.duplicated().sum()))
print(df[df.duplicated(keep=False)].sort_values("customer_id").head(10))

section("5. Remove duplicates - drop_duplicates()")
df = df.drop_duplicates()
print("Shape after drop_duplicates():", df.shape)

# ------------------------------------------------------------- TEXT CLEANING
section("6. Clean customer names - str.strip() + str.title()")
print("Before:", df["name"].head(5).tolist())
df["name"] = df["name"].str.strip().str.lower().str.title()
print("After :", df["name"].head(5).tolist())

section("7. Clean cities - str.strip() + str.title()")
print("Before (unique):", sorted(df["city"].dropna().unique().tolist()))
df["city"] = df["city"].str.strip().str.title()
print("After  (unique):", sorted(df["city"].unique().tolist()))

section("8. Clean emails - str.strip() + str.lower()")
print("Before:", df["email"].head(5).tolist())
df["email"] = df["email"].str.strip().str.lower()
print("After :", df["email"].head(5).tolist())

section("9. str.upper() demo - city codes")
df["city_code"] = df["city"].str[:3].str.upper()
print(df[["city", "city_code"]].head(5))

# -------------------------------------------------------------- REPLACE / TYPES
section("10. replace() - strip currency symbols and commas from purchase_amount")
print("Before:", df["purchase_amount"].head(8).tolist())
df["purchase_amount"] = (
    df["purchase_amount"]
    .replace({r"Rs\.": "", ",": "", r"\s+": ""}, regex=True)
)
print("After :", df["purchase_amount"].head(8).tolist())

# ------------------------------------------------------- HANDLE MISSING VALUES
section("11. dropna() - drop rows missing a customer_id or name (critical fields)")
print("Shape before dropna:", df.shape)
df = df.dropna(subset=["customer_id", "name"])
print("Shape after  dropna:", df.shape)

section("12. fillna() - fill remaining missing values")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df["age"] = df["age"].fillna(df["age"].median())
df["purchase_amount"] = df["purchase_amount"].fillna(df["purchase_amount"].mean().round(2))
df["rating"] = df["rating"].fillna(df["rating"].mean().round(1))
df["email"] = df["email"].fillna("not_provided@example.com")
df["city"] = df["city"].fillna("Unknown")

print("Missing values after fillna():")
print(df.isnull().sum())

section("13. astype() - convert columns to correct data types")
print("Types before astype():")
print(df.dtypes)

df["age"] = df["age"].astype(int)
df["purchase_amount"] = df["purchase_amount"].astype(float)
df["rating"] = df["rating"].astype(float)
df["customer_id"] = df["customer_id"].astype("string")
df["city"] = df["city"].astype("category")

print("\nTypes after astype():")
print(df.dtypes)

# ------------------------------------------------------------------ COMPARISON
shape_after = df.shape

section("14. Shape comparison - before vs after cleaning")
comparison = pd.DataFrame(
    {
        "rows": [shape_before[0], shape_after[0]],
        "columns": [shape_before[1], shape_after[1]],
    },
    index=["before_cleaning", "after_cleaning"],
)
print(comparison)
print("\nRows removed:", shape_before[0] - shape_after[0])

section("C. CLEAN DATASET - AFTER CLEANING")
print(df.head(15))

section("D. describe() on cleaned numeric data")
print(df.describe())

# 15. Save
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)
print(f"\nCleaned dataset saved to: {OUTPUT_PATH}")
