class Commodity:
    def __init__(self,commodity_id,commodity_name,commodity_price,commodity_total_number,commodity_number):
        self.id = commodity_id
        self.name = commodity_name
        self.price = commodity_price
        self.total_number = commodity_total_number
        self.number = commodity_number

    def display(self):
        print(f"商品序号: {self.id}")
        print(f"商品名: {self.name}")
        print(f"单价: {self.price} 元")
        print(f"总数量: {self.total_number}")
        print(f"剩余数量: {self.number}")

    def income(self):
        income = self.price * (self.total_number - self.number)
        print(income)

    def setdata(self,id,name,price,total_number,number):
        self.id = id
        self.name = name
        self.price = price
        self.total_number = total_number
        self.number = number

