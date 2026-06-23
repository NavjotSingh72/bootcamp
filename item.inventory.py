class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

product_data = [
    ("Phone", 50000, 2),
    ("Charger", 500, 10),
    ("Tablet", 10000, 5)
]

products = []

for name, price, quantity in product_data:
    product = Product(name, price, quantity)
    products.append(product)

grand_total = 0

for product in products:
    value = product.total_value()
    print(f"{product.name} Total Value = {value}")
    grand_total += value

print("Grand Total Inventory Value =", grand_total)