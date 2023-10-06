class Commodity:
    def __init__(self,commodity_id,commodity_name,commodity_price,commodity_total_number,commodity_number):
        self.id = commodity_id
        self.name = commodity_name
        self.price = commodity_price
        self.total_number = commodity_total_number
        self.number = commodity_number

    def display(self):
        print(f"信息{self.id,self.name,self.price,self.total_number,self.number}")

    def income(self):
        income = self.price * (self.total_number - self.number)
        print(income)

    def setdata(self,id,name,price,total_number,number):
        self.id = id
        self.name = name
        self.price = price
        self.total_number = total_number
        self.number = number