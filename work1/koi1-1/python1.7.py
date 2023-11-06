class Product:
    def __init__(self, product_id, product_name, unit_price, total_quantity, remaining_quantity):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__unit_price = unit_price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = remaining_quantity
    def display(self):
        print("商品序号:", self.__product_id)
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
product1 = Product(1, "笔", 10.0, 100, 80)
product1.display()
print(f"已售出商品价值:{product1.income()}")
product1.setdata("笔记本", 15.0, 150, 120)
product1.display()
