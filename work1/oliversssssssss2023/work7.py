#设计一个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。具有的 公有成员函数是：初始化
#商品信息的构造函数init，显示商品
#信息的函数cisplay，计算已售出 商品价值
#iincome， 修改商品信息的函数setdata
class Product:
    def __init__(self,product_id, product_name, product_price, total_quantity, remaining_quantity):
        self.product_id = product_id
        self.product_name = product_name  
        self.product_price = product_price
        self.total_quantity = total_quantity
        self.remaining_quantity = remaining_quantity

    def display(self):
        print("商品序号：",self.product_id)
        print("商品名称：",self.product_name)
        print("商品价格:",self.product_price)
        print("商品数量:",self.total_quantity)
        print("商品剩余数量:" ,self.remaining_quantity)
    def calculate_income(self):
        sold_quantity = self.total_quantity - self.remaining_quantity
        sold_price = self.product_price * sold_quantity
        return sold_price
    def set_date(self,unit_price,remaining_quantity):
        self.unit_price = unit_price 
        self.remaining_quantity = remaining_quantity

Product1= Product(1,"西瓜",10,100,10)
Product1.display()
income= Product1.calculate_income()
print("商品总收入为",income)
Product1.set_date(2,3)
Product1.display()

