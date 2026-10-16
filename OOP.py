class Product:
    def __init__ (self, product_id, name, price, quantity, manufacture_date):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__manufacture_date = manufacture_date

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_price(self, price):
        if price >= 0:
            self.__price = price

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity

    def display_info(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price}")
        print(f"Quantity: {self.__quantity}")
        print(f"Manufacture Date: {self.__manufacture_date}")