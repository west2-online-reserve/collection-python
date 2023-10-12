class Product:
    def __init__(self,idcard,name,price,total,remain):
        self.idcard = idcard
        self.name = name  
        self.price = price
        self.total = total
        self.remain = remain
    def display(self):
        print("商品序号：",self.idcard)
        print("商品名称：",self.name)
        print("商品价格:",self.price)
        print("商品数量:",self.total)
        print("商品剩余数量:" ,self.remain)
    def income(self):
        sold = self.total - self.remain
        soldprice = self.price * sold
        return soldprice
    def setdata(self,unitprice,remain):
        self.unitprice = unitprice 
        self.remain = remain