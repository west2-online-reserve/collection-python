# Author : AnnieHathaway
class Product:
    def __init__(self, id, name, price, quantity):
        # 私有成员
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__remaining_quantity = quantity

    def display(self):
        print("商品序号:", self.__id)
        print("商品名称:", self.__name)
        print("单价:", self.__price)
        print("总数量:", self.__quantity)
        print("剩余数量:", self.__remaining_quantity)

    def income(self, sold_quantity):
        return sold_quantity * self.__price

    def setdata(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__remaining_quantity = quantity


# 演示一下
product1 = Product(1, "吃的", 9.9, 100)
product1.display()
print("销售额:", product1.income(20))

print("修改后:")
product1.setdata("商品B", 12.0, 150)
product1.display()
