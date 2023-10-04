class Product:
    def __init__(self, serial_number, name, price, total_quantity, remaining_quantity):
        self.__serial_number = serial_number
        self.__name = name
        self.__price = price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = remaining_quantity

    def display(self):
        print("Serial Number:", self.__serial_number)
        print("Name:", self.__name)
        print("Price:", self.__price)
        print("Total Quantity:", self.__total_quantity)
        print("Remaining Quantity:", self.__remaining_quantity)

    def income(self):
        return self.__price * (self.__total_quantity - self.__remaining_quantity)

    def setdata(self, serial_number, name, price, total_quantity, remaining_quantity):
        self.__serial_number = serial_number
        self.__name = name
        self.__price = price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = remaining_quantity


product = Product(1, "Apple", 2.5, 100, 50)
product.display()
income = product.income()
print("Income:", income)

