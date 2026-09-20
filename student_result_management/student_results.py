"""Student Result Management Using Pandas."""

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "students.csv"
OUTPUT_PATH = BASE_DIR / "output" / "student_results.csv"


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# 1. Read the CSV file
df = pd.read_csv(CSV_PATH)

section("1. First 5 records - head()")
print(df.head())

section("2. Last 5 records - tail()")
print(df.tail())

section("3. Dataset shape (rows, columns)")
print(df.shape)

section("4. Column names")
print(list(df.columns))

section("5. Data types")
print(df.dtypes)

section("6. info()")
df.info()

section("7. describe()")
print(df.describe())

section("8. Average marks")
print("Average Python marks :", round(df["python_marks"].mean(), 2))
print("Average SQL marks    :", round(df["sql_marks"].mean(), 2))
print("Average Pandas marks :", round(df["pandas_marks"].mean(), 2))

section("9. Maximum marks in each subject")
print(df[["python_marks", "sql_marks", "pandas_marks"]].max())

section("10. Minimum marks in each subject")
print(df[["python_marks", "sql_marks", "pandas_marks"]].min())

section("11. Students sorted by Python marks (highest first)")
print(df.sort_values("python_marks", ascending=False))

section("12. Students sorted by attendance (highest first)")
print(df.sort_values("attendance", ascending=False))

section("13. Students with Python marks > 80")
print(df[df["python_marks"] > 80])

section("14. Students with attendance > 75")
print(df[df["attendance"] > 75])

section("15. Selected columns: name, python_marks, pandas_marks")
print(df[["name", "python_marks", "pandas_marks"]])

# 16 & 17. New columns
df["total_marks"] = df["python_marks"] + df["sql_marks"] + df["pandas_marks"]
df["average_marks"] = (df["total_marks"] / 3).round(2)

section("16. Dataset with total_marks and average_marks")
print(df.head())

# 18. Save processed dataset
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)
print(f"\nProcessed dataset saved to: {OUTPUT_PATH}")
