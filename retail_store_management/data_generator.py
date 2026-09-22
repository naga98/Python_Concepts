"""Part 2 & 3 - Build products.csv and sales.csv using file handling."""

import csv
import random
from pathlib import Path

from products import Books, Clothing, Electronics, Product

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
PRODUCTS_CSV = DATA_DIR / "products.csv"
SALES_CSV = DATA_DIR / "sales.csv"

FIELDS = ["product_id", "name", "brand", "category", "price", "stock",
          "warranty", "model", "size", "material", "author", "publisher"]

random.seed(7)

CITIES = ["Bangalore", "Mumbai", "Delhi", "Chennai", "Pune", "Hyderabad", "Kolkata", "Jaipur"]
PAYMENTS = ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery", "Wallet"]


def build_initial_products():
    """First batch of products, created as objects of the child classes."""
    return [
        Electronics("E001", "Dell Inspiron 15 Laptop", "Dell", 54990, 25, 2, "INS-15-3520"),
        Electronics("E002", "HP Pavilion 14 Laptop", "HP", 62990, 18, 2, "PAV-14-EC1"),
        Electronics("E003", "Apple MacBook Air M2", "Apple", 114900, 9, 1, "MBA-M2-256"),
        Electronics("E004", "Samsung Galaxy S24", "Samsung", 74999, 35, 1, "SM-S921B"),
        Electronics("E005", "Apple iPhone 15", "Apple", 79900, 22, 1, "A3090"),
        Electronics("E006", "Sony WH-1000XM5 Headphones", "Sony", 29990, 14, 2, "WH1000XM5"),
        Electronics("E007", "LG UltraGear Monitor 27", "LG", 38990, 7, 3, "27GP850"),
        Electronics("E008", "Logitech MX Master 3S Mouse", "Logitech", 9495, 40, 1, "MX3S"),
        Electronics("E009", "Keychron K2 Keyboard", "Keychron", 8499, 16, 1, "K2-V2"),
        Electronics("E010", "Samsung Galaxy Tab S9", "Samsung", 72999, 6, 1, "SM-X710"),
        Clothing("C001", "Cotton Casual Shirt", "Allen Solly", 1799, 60, "M", "Cotton"),
        Clothing("C002", "Slim Fit Denim Jeans", "Levis", 3499, 45, "32", "Denim"),
        Clothing("C003", "Round Neck T-Shirt", "Puma", 999, 120, "L", "Cotton Blend"),
        Clothing("C004", "Formal Blazer", "Raymond", 6999, 12, "40", "Polyester Wool"),
        Clothing("C005", "Winter Hoodie", "Nike", 2999, 38, "XL", "Fleece"),
        Clothing("C006", "Running Shorts", "Adidas", 1499, 8, "M", "Polyester"),
        Clothing("C007", "Silk Saree", "Nalli", 8999, 15, "Free", "Silk"),
        Clothing("C008", "Kurta Set", "Fabindia", 2499, 27, "L", "Khadi Cotton"),
        Books("B001", "Python Crash Course", "No Starch Press", 2499, 50, "Eric Matthes", "No Starch Press"),
        Books("B002", "Fluent Python", "OReilly", 3999, 20, "Luciano Ramalho", "OReilly Media"),
        Books("B003", "Clean Code", "Pearson", 3200, 33, "Robert C. Martin", "Prentice Hall"),
        Books("B004", "Atomic Habits", "Penguin", 699, 150, "James Clear", "Penguin Random House"),
        Books("B005", "The Alchemist", "HarperCollins", 399, 200, "Paulo Coelho", "HarperCollins"),
        Books("B006", "Sapiens", "Vintage", 899, 5, "Yuval Noah Harari", "Vintage Books"),
        Books("B007", "Data Science from Scratch", "OReilly", 2899, 18, "Joel Grus", "OReilly Media"),
    ]


def build_extra_products():
    """Second batch, appended to the existing file to demonstrate append mode."""
    return [
        Electronics("E011", "Canon EOS 1500D Camera", "Canon", 41999, 4, 2, "EOS-1500D"),
        Electronics("E012", "boAt Rockerz 550", "boAt", 2499, 95, 1, "RKZ-550"),
        Clothing("C009", "Leather Jacket", "Woodland", 7499, 6, "L", "Genuine Leather"),
        Clothing("C010", "Sports Track Pants", "Reebok", 1899, 52, "M", "Polyester"),
        Books("B008", "Rich Dad Poor Dad", "Plata", 450, 180, "Robert Kiyosaki", "Plata Publishing"),
        Books("B009", "Deep Work", "Piatkus", 799, 9, "Cal Newport", "Piatkus Books"),
        Books("B010", "The Pragmatic Programmer", "Pearson", 3499, 11, "Andrew Hunt", "Addison-Wesley"),
    ]


def write_products(items):
    """Create the file and write the header + first batch (write mode 'w')."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PRODUCTS_CSV, "w", encoding="utf-8", newline="") as f:  # context manager
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for item in items:
            writer.writerow(item.to_dict())
    print(f"Created {PRODUCTS_CSV.name} and wrote {len(items)} products (mode='w').")


def append_products(items):
    """Append more products to the existing file (append mode 'a')."""
    with open(PRODUCTS_CSV, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        for item in items:
            writer.writerow(item.to_dict())
    print(f"Appended {len(items)} more products (mode='a').")


def read_products():
    """Read the product records back with plain file handling (read mode 'r')."""
    with open(PRODUCTS_CSV, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    print(f"Read {len(rows)} product records from {PRODUCTS_CSV.name} (mode='r').")
    return rows


def rows_to_objects(rows):
    """Rebuild child-class objects from the CSV rows (demonstrates polymorphism)."""
    objects = []
    for row in rows:
        if row["category"] == "Electronics":
            obj = Electronics(row["product_id"], row["name"], row["brand"], row["price"],
                              row["stock"], row["warranty"], row["model"])
        elif row["category"] == "Clothing":
            obj = Clothing(row["product_id"], row["name"], row["brand"], row["price"],
                           row["stock"], row["size"], row["material"])
        elif row["category"] == "Books":
            obj = Books(row["product_id"], row["name"], row["brand"], row["price"],
                        row["stock"], row["author"], row["publisher"])
        else:
            obj = Product(row["product_id"], row["name"], row["brand"], row["price"], row["stock"])
        objects.append(obj)
    return objects


def generate_sales(product_rows, count=60):
    """Create sales.csv with random transactions drawn from the product catalogue."""
    with open(SALES_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["transaction_id", "product_id", "product_name", "category",
                         "quantity", "price", "customer_city", "payment_method"])
        for i in range(1, count + 1):
            p = random.choice(product_rows)
            qty = random.randint(1, 5) if float(p["price"]) < 10000 else random.randint(1, 2)
            writer.writerow([
                f"T{i:04d}", p["product_id"], p["name"], p["category"],
                qty, p["price"], random.choice(CITIES), random.choice(PAYMENTS),
            ])
    print(f"Created {SALES_CSV.name} with {count} transactions.")


def main():
    print("=" * 70)
    print("PART 2 - PRODUCT FILE (file handling)")
    print("=" * 70)
    write_products(build_initial_products())
    append_products(build_extra_products())
    rows = read_products()

    print("\nSample products displayed via overridden display_product():")
    for obj in rows_to_objects(rows)[:2] + rows_to_objects(rows)[10:11] + rows_to_objects(rows)[18:19]:
        obj.display_product()

    print("\nupdate_stock() demo:")
    sample = rows_to_objects(rows)[0]
    print("  Stock before sale of 3 units:", sample.stock)
    print("  Stock after  sale of 3 units:", sample.update_stock(-3))
    print("  Stock after  restock of 10  :", sample.update_stock(10))

    print("\n" + "=" * 70)
    print("PART 3 - SALES DATA")
    print("=" * 70)
    generate_sales(rows, count=60)


if __name__ == "__main__":
    main()
