class Goods:
    def __init__(self, product_id, product_name, unit_price, total_quantity):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__unit_price = unit_price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = total_quantity
    def display(self):
        print(f"商品序号: {self.__product_id}")
        print(f"商品名: {self.__product_name}")
        print(f"单价: {self.__unit_price}")
        print(f"总数量: {self.__total_quantity}")
        print(f"剩余数量: {self.__remaining_quantity}")
    def income(self, sold_quantity):
        if sold_quantity > self.__remaining_quantity:
            print("销售数量超过剩余数量！")
            return
        self.__remaining_quantity -= sold_quantity
        return sold_quantity * self.__unit_price
    def setdata(self, product_id=None, product_name=None, unit_price=None, total_quantity=None):
        if product_id:
            self.__product_id = product_id
        if product_name:
            self.__product_name = product_name
        if unit_price:
            self.__unit_price = unit_price
        if total_quantity:
            self.__total_quantity = total_quantity
            self.__remaining_quantity = total_quantity
"""具体数据"""
goods = Goods(101, "苹果", 0.5, 100)
goods.display()
print(f"卖了20个的income: {goods.income(20)}")
goods.setdata(product_name="香蕉", total_quantity=150)
goods.display()