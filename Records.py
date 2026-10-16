class Product:
    def __init__(self, name, price, expiration_date, is_dairy):
        self.name = name
        self.price = price
        self.expiration_date = expiration_date
        self.is_dairy = is_dairy

#Instatiating a product record
product1 = Product(name="Milk", price=2.99, expiration_date="2024-02-10", is_dairy=True)

#Accessing fields of the Product record
print(product1.name)
print(product1.price)
print(product1.expiration_date)
print(product1.is_dairy)

#Modifying the field of the product record
product1.name = "Australia Milk"
print(product1.name)