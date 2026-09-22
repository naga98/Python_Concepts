"""Part 4 & 5 - Pandas analysis of the retail store data and report generation."""

from pathlib import Path

import pandas as pd

pd.set_option("display.width", 160)
pd.set_option("display.max_columns", 20)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def load_data():
    products = pd.read_csv(DATA_DIR / "products.csv")
    sales = pd.read_csv(DATA_DIR / "sales.csv")
    return products, sales


def clean_sales(sales):
    """Basic cleaning: trim text, drop duplicates/nulls, fix data types."""
    before = sales.shape
    for col in ["product_id", "product_name", "category", "customer_city", "payment_method"]:
        sales[col] = sales[col].astype(str).str.strip()

    sales = sales.drop_duplicates(subset="transaction_id")
    sales = sales.dropna(subset=["product_id", "quantity", "price"])
    sales["quantity"] = sales["quantity"].astype(int)
    sales["price"] = sales["price"].astype(float)
    sales["revenue"] = sales["quantity"] * sales["price"]

    section("DATA CLEANING")
    print("Missing values per column:")
    print(sales.isnull().sum())
    print("\nDuplicate transaction ids:", int(sales.duplicated(subset='transaction_id').sum()))
    print("Shape before cleaning:", before)
    print("Shape after  cleaning:", sales.shape)
    return sales


def analyse(products, sales):
    """Runs every required analysis and returns the values needed for reports."""
    section("INSPECT DATA")
    print(sales.head())
    print("\nShape:", sales.shape)
    print("Columns:", list(sales.columns))
    sales.info()
    print("\ndescribe():")
    print(sales.describe())

    section("1-6. HEADLINE SALES METRICS")
    total_transactions = len(sales)
    total_quantity = int(sales["quantity"].sum())
    total_revenue = float(sales["revenue"].sum())
    avg_transaction = float(sales["revenue"].mean())
    highest = sales.loc[sales["revenue"].idxmax()]
    lowest = sales.loc[sales["revenue"].idxmin()]

    print("Total sales transactions :", total_transactions)
    print("Total quantity sold      :", total_quantity)
    print(f"Total revenue            : Rs.{total_revenue:,.2f}")
    print(f"Average transaction value: Rs.{avg_transaction:,.2f}")
    print("\nHighest-value transaction:")
    print(highest)
    print("\nLowest-value transaction:")
    print(lowest)

    section("7-8. BEST AND LOWEST SELLING PRODUCTS (by quantity)")
    qty_by_product = sales.groupby("product_name")["quantity"].sum().sort_values(ascending=False)
    best_product = qty_by_product.index[0]
    worst_product = qty_by_product.index[-1]
    print(qty_by_product)
    print("\nBest-selling product  :", best_product, f"({qty_by_product.iloc[0]} units)")
    print("Lowest-selling product:", worst_product, f"({qty_by_product.iloc[-1]} units)")

    section("9. SALES (QUANTITY) CATEGORY-WISE")
    qty_by_category = sales.groupby("category")["quantity"].sum().sort_values(ascending=False)
    print(qty_by_category)

    section("10. REVENUE CATEGORY-WISE")
    revenue_by_category = sales.groupby("category")["revenue"].sum().sort_values(ascending=False)
    print(revenue_by_category)

    section("11. REVENUE PRODUCT-WISE")
    revenue_by_product = sales.groupby("product_name")["revenue"].sum().sort_values(ascending=False)
    print(revenue_by_product)

    section("12. REVENUE CITY-WISE")
    revenue_by_city = sales.groupby("customer_city")["revenue"].sum().sort_values(ascending=False)
    print(revenue_by_city)

    section("13. PAYMENT-METHOD DISTRIBUTION")
    payment_counts = sales["payment_method"].value_counts()
    payment_share = (payment_counts / total_transactions * 100).round(2)
    print(pd.DataFrame({"transactions": payment_counts, "share_percent": payment_share}))

    section("14. TOP 5 PRODUCTS BY REVENUE")
    print(revenue_by_product.head(5))

    section("15. BOTTOM 5 PRODUCTS BY REVENUE")
    print(revenue_by_product.tail(5))

    section("16-18. PRODUCT CATALOGUE PRICE STATS")
    avg_price = float(products["price"].mean())
    print(f"Average product price: Rs.{avg_price:,.2f}")
    print(f"Maximum product price: Rs.{products['price'].max():,.2f} "
          f"({products.loc[products['price'].idxmax(), 'name']})")
    print(f"Minimum product price: Rs.{products['price'].min():,.2f} "
          f"({products.loc[products['price'].idxmin(), 'name']})")

    section("19. PRODUCTS WITH STOCK BELOW 10")
    low_stock = products[products["stock"] < 10][["product_id", "name", "category", "stock"]]
    print(low_stock)

    section("20. PRODUCTS PRICED ABOVE THE AVERAGE PRICE")
    above_avg = products[products["price"] > avg_price][["product_id", "name", "category", "price"]]
    print(above_avg.sort_values("price", ascending=False))

    section("SORTING EXAMPLES")
    print("Transactions sorted by revenue (top 5):")
    print(sales.sort_values("revenue", ascending=False).head(5))
    print("\nProducts sorted by stock (lowest 5):")
    print(products.sort_values("stock").head(5)[["name", "category", "stock"]])

    section("PANDAS SERIES vs DATAFRAME")
    print("sales['revenue'] is a", type(sales["revenue"]).__name__)
    print(sales["revenue"].head(3))
    print("\nsales[['revenue']] is a", type(sales[["revenue"]]).__name__)
    print(sales[["revenue"]].head(3))

    return {
        "total_transactions": total_transactions,
        "total_quantity": total_quantity,
        "total_revenue": total_revenue,
        "avg_transaction": avg_transaction,
        "highest": highest,
        "lowest": lowest,
        "best_product": best_product,
        "worst_product": worst_product,
        "qty_by_product": qty_by_product,
        "qty_by_category": qty_by_category,
        "revenue_by_category": revenue_by_category,
        "revenue_by_product": revenue_by_product,
        "revenue_by_city": revenue_by_city,
        "payment_counts": payment_counts,
        "avg_price": avg_price,
        "low_stock": low_stock,
    }


def generate_reports(products, sales, stats):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sales.to_csv(OUTPUT_DIR / "cleaned_sales.csv", index=False)

    product_report = (
        sales.groupby(["product_id", "product_name", "category"])
        .agg(units_sold=("quantity", "sum"),
             transactions=("transaction_id", "count"),
             revenue=("revenue", "sum"))
        .reset_index()
        .sort_values("revenue", ascending=False)
    )
    product_report = product_report.merge(
        products[["product_id", "brand", "price", "stock"]], on="product_id", how="left"
    )
    product_report.to_csv(OUTPUT_DIR / "product_report.csv", index=False)

    city_report = (
        sales.groupby("customer_city")
        .agg(transactions=("transaction_id", "count"),
             units_sold=("quantity", "sum"),
             revenue=("revenue", "sum"),
             avg_transaction_value=("revenue", "mean"))
        .round(2)
        .reset_index()
        .sort_values("revenue", ascending=False)
    )
    city_report.to_csv(OUTPUT_DIR / "city_sales_report.csv", index=False)

    category_report = (
        sales.groupby("category")
        .agg(transactions=("transaction_id", "count"),
             units_sold=("quantity", "sum"),
             revenue=("revenue", "sum"),
             avg_transaction_value=("revenue", "mean"))
        .round(2)
        .reset_index()
        .sort_values("revenue", ascending=False)
    )
    category_report.to_csv(OUTPUT_DIR / "category_report.csv", index=False)

    summary_path = OUTPUT_DIR / "sales_summary.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("=" * 55 + "\n")
        f.write("RETAIL STORE SALES REPORT\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"Total Transactions       : {stats['total_transactions']}\n")
        f.write(f"Total Quantity Sold      : {stats['total_quantity']}\n")
        f.write(f"Total Revenue            : Rs.{stats['total_revenue']:,.2f}\n")
        f.write(f"Average Transaction Value: Rs.{stats['avg_transaction']:,.2f}\n\n")
        f.write(f"Highest-Value Transaction: {stats['highest']['transaction_id']} - "
                f"{stats['highest']['product_name']} (Rs.{stats['highest']['revenue']:,.2f})\n")
        f.write(f"Lowest-Value Transaction : {stats['lowest']['transaction_id']} - "
                f"{stats['lowest']['product_name']} (Rs.{stats['lowest']['revenue']:,.2f})\n\n")
        f.write(f"Best Selling Product     : {stats['best_product']}\n")
        f.write(f"Lowest Selling Product   : {stats['worst_product']}\n")
        f.write(f"Highest Revenue Category : {stats['revenue_by_category'].index[0]} "
                f"(Rs.{stats['revenue_by_category'].iloc[0]:,.2f})\n")
        f.write(f"Highest Revenue City     : {stats['revenue_by_city'].index[0]} "
                f"(Rs.{stats['revenue_by_city'].iloc[0]:,.2f})\n")
        f.write(f"Most Used Payment Method : {stats['payment_counts'].index[0]} "
                f"({stats['payment_counts'].iloc[0]} transactions)\n\n")

        f.write("-" * 55 + "\nREVENUE BY CATEGORY\n" + "-" * 55 + "\n")
        for name, value in stats["revenue_by_category"].items():
            f.write(f"  {name:<15} Rs.{value:>14,.2f}\n")

        f.write("\n" + "-" * 55 + "\nREVENUE BY CITY\n" + "-" * 55 + "\n")
        for name, value in stats["revenue_by_city"].items():
            f.write(f"  {name:<15} Rs.{value:>14,.2f}\n")

        f.write("\n" + "-" * 55 + "\nTOP 5 PRODUCTS BY REVENUE\n" + "-" * 55 + "\n")
        for name, value in stats["revenue_by_product"].head(5).items():
            f.write(f"  {name:<32} Rs.{value:>14,.2f}\n")

        f.write("\n" + "-" * 55 + "\nLOW STOCK ALERT (stock < 10)\n" + "-" * 55 + "\n")
        for _, row in stats["low_stock"].iterrows():
            f.write(f"  {row['name']:<32} {row['stock']:>3} left\n")

        f.write("\n" + "=" * 55 + "\nEND OF REPORT\n" + "=" * 55 + "\n")

    section("PART 5 - REPORTS GENERATED")
    for path in sorted(OUTPUT_DIR.iterdir()):
        print(" -", path.relative_to(BASE_DIR))

    print("\nContents of sales_summary.txt:\n")
    with open(summary_path, "r", encoding="utf-8") as f:
        print(f.read())


def main():
    products, sales = load_data()
    sales = clean_sales(sales)
    stats = analyse(products, sales)
    generate_reports(products, sales, stats)


if __name__ == "__main__":
    main()
