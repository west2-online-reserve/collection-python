class Product:
    def __init__(self, number, name, price, total):
        self.__number = number
        self.__name = name
        self.__price = price
        self.__total = total
        self.__remain = total

    def display(self):
        print(f"商品序号：{self.__number}")
        print(f"商品名：{self.__name}")
        print(f"单价：{self.__price}")
        print(f"总数量：{self.__total}")
        print(f"剩余数量：{self.__remain}")

    def income(self, sold):
        if sold <= self.__total:
            value = sold * self.__price
            self.__remain -= sold
            return value
        else:
            print("库存不足")

    def setdata(self, price, total, remain):
        self.__price = price
        self.__total = total
        self.__remain = remain


product1 = Product(1, "PYTHON", 100, 10)
income1 = product1.income(5)
product1.display()
print(f"售出收入:{income1}")



