class Product:
    def __init__(self, product_number, product_name, unit_price, total_quantity, remaining_quantity):
        self.__product_number = product_number
        self.__product_name = product_name
        self.__unit_price = unit_price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = remaining_quantity

    def display(self):
        print("商品序号:", self.__product_number)
        print("商品名:", self.__product_name)
        print("单价:", self.__unit_price)
        print("总数量:", self.__total_quantity)
        print("剩余数量:", self.__remaining_quantity)

    def income(self):
        return self.__unit_price * (self.__total_quantity - self.__remaining_quantity)

    def setdata(self, product_name, unit_price, total_quantity, remaining_quantity):
        self.__product_name = product_name
        self.__unit_price = unit_price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = remaining_quantity

# 示例用法
product1 = Product(1, "商品A", 10.0, 100, 50)
product1.display()
print("已售出商品价值:", product1.income())

# 修改商品信息
product1.setdata("商品A（改进版）", 12.0, 150, 75)
product1.display()
print("已售出商品价值:", product1.income())
