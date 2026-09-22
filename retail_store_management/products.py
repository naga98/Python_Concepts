"""Part 1 - Product classes with inheritance and method overriding."""


class Product:
    """Parent class for every item sold by the retail store."""

    category = "General"

    def __init__(self, product_id, name, brand, price, stock):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = float(price)
        self.stock = int(stock)

    def display_product(self):
        print(f"[{self.product_id}] {self.name} | Brand: {self.brand} "
              f"| Rs.{self.price:,.2f} | Stock: {self.stock}")

    def update_stock(self, quantity):
        """Positive quantity restocks, negative quantity records a sale."""
        new_stock = self.stock + quantity
        if new_stock < 0:
            raise ValueError(f"Not enough stock for {self.name}: have {self.stock}, need {-quantity}")
        self.stock = new_stock
        return self.stock

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "price": self.price,
            "stock": self.stock,
            "warranty": "",
            "model": "",
            "size": "",
            "material": "",
            "author": "",
            "publisher": "",
        }


class Electronics(Product):
    category = "Electronics"

    def __init__(self, product_id, name, brand, price, stock, warranty, model):
        super().__init__(product_id, name, brand, price, stock)
        self.warranty = warranty
        self.model = model

    def display_product(self):  # method overriding
        super().display_product()
        print(f"    Category: {self.category} | Model: {self.model} | Warranty: {self.warranty} year(s)")

    def to_dict(self):
        data = super().to_dict()
        data["warranty"] = self.warranty
        data["model"] = self.model
        return data


class Clothing(Product):
    category = "Clothing"

    def __init__(self, product_id, name, brand, price, stock, size, material):
        super().__init__(product_id, name, brand, price, stock)
        self.size = size
        self.material = material

    def display_product(self):  # method overriding
        super().display_product()
        print(f"    Category: {self.category} | Size: {self.size} | Material: {self.material}")

    def to_dict(self):
        data = super().to_dict()
        data["size"] = self.size
        data["material"] = self.material
        return data


class Books(Product):
    category = "Books"

    def __init__(self, product_id, name, brand, price, stock, author, publisher):
        super().__init__(product_id, name, brand, price, stock)
        self.author = author
        self.publisher = publisher

    def display_product(self):  # method overriding
        super().display_product()
        print(f"    Category: {self.category} | Author: {self.author} | Publisher: {self.publisher}")

    def to_dict(self):
        data = super().to_dict()
        data["author"] = self.author
        data["publisher"] = self.publisher
        return data
