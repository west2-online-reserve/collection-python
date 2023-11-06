class commodity:
    def __init__(self,ids,name,price,totalnum,restnum):
        self.ids=ids
        self.name=name
        self.price=price
        self.totalnum=totalnum
        self.restnum=restnum

    def display(self):
        print("商品编号：%s\n商品名称：%s\n商品单价：%s\n商品总数量：%s\n商品剩余数量：%s\n"%(self.ids,self.name,self.price,self.totalnum,self.restnum))

    def income(self):
        print("商品总价：%s"%(self.price*(self.totalnum-self.restnum)))

    def setdata(self):
        self.ids=input("ids:")
        self.name=input("name:")
        self.price=input("price")
        self.totalnum=input("totalnum=")
        self.restnum=input("restnum=")
