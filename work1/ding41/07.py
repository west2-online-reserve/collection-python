class Commodity:
    def __init__(self,number,name,money,all,rest):
        self.__number=number
        self.__name=name
        self.__money=money
        self.__all=all
        self.__rest=rest
    def display(self):
        print(f"商品信息：\n编号:{self.__number}\n商品名:{self.__name}")
        print(f"单价：{self.__money}\n总数量:{self.__all}\n剩下:{self.__rest}")
    def income(self):
        print(f"营业额为{self.__money * (self.__all-self.__rest)}")
    def setdata(self):
        self.__money+=5

commodity=Commodity(123,"笔",5,1000,500)
commodity.display()
commodity.income()
commodity.setdata()
commodity.display()