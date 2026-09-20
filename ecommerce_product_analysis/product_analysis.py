from pathlib import Path

import pandas as pd

pd.set_option("display.width", 160)
pd.set_option("display.max_columns", 20)

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "products.csv"
OUTPUT_PATH = BASE_DIR / "output" / "final_products.csv"


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# 1. Read CSV
df = pd.read_csv(CSV_PATH)

section("1. Inspect dataset - head()")
print(df.head())

section("2. Inspect dataset - tail()")
print(df.tail())

section("3. Shape / columns / data types")
print("Shape   :", df.shape)
print("Columns :", list(df.columns))
print("\nData types:")
print(df.dtypes)

section("4. info()")
df.info()

section("5. describe()")
print(df.describe())

section("6. Total products")
print(len(df))

section("7. Unique categories")
print(df["category"].unique())
print("Total categories:", df["category"].nunique())

section("8. Unique brands")
print(df["brand"].unique())
print("Total brands:", df["brand"].nunique())

section("9. Product count category-wise")
print(df["category"].value_counts())

section("10. Average price of all products")
print(round(df["price"].mean(), 2))

section("11. Highest-priced product")
print(df.loc[df["price"].idxmax()])

section("12. Lowest-priced product")
print(df.loc[df["price"].idxmin()])

section("13. Products priced above Rs.50,000")
print(df[df["price"] > 50000][["product_name", "category", "brand", "price"]])

section("14. Products with rating greater than 4")
print(df[df["rating"] > 4][["product_name", "brand", "rating"]])

section("15. Products sorted by price (highest first)")
print(df.sort_values("price", ascending=False)[["product_name", "category", "price"]])

section("16. Products sorted by rating (highest first)")
print(df.sort_values("rating", ascending=False)[["product_name", "brand", "rating"]])

section("17. Products with stock below 10")
print(df[df["stock"] < 10][["product_name", "category", "stock"]])

# 18 & 19. Derived columns
df["discount_amount"] = (df["price"] * df["discount"] / 100).round(2)
df["final_price"] = (df["price"] - df["discount_amount"]).round(2)

section("18. discount_amount and final_price")
print(df[["product_name", "price", "discount", "discount_amount", "final_price"]].head(10))

section("19. Average price by category")
print(df.groupby("category")["price"].mean().round(2).sort_values(ascending=False))

section("20. Average rating by brand")
print(df.groupby("brand")["rating"].mean().round(2).sort_values(ascending=False))

section("21. Maximum product price category-wise")
print(df.groupby("category")["price"].max().sort_values(ascending=False))

# 22. Export final data
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)
print(f"\nFinal dataset exported to: {OUTPUT_PATH}")

