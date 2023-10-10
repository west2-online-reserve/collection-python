class goods:
    def __init__(self,num,name,price,total_number,number) -> None:
        self.num=num
        self.name=name
        self.price=price
        self.total_number=total_number
        self.number=number
    def display(self):
        print("商品编号：%s\n商品名称：%s\n商品单价：%s\n商品库存：%s\n商品数量：%s\n"%(self.num,self.name,self.price,self.total_number,self.number))
    def income(self):
        print("商品总价：%s"%(self.price*(self.total_number-self.number)))
    def setdata(self):
        self.num=input('num:')
        self.name=input('name:')
        self.price=input('price:')
        self.total_number=input('total_number:')
        self.number=input('number:')