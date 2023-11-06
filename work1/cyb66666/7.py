#设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。
#具有的公有成员函数是：初始化商品信息的构造函数__init__，显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata
class commodity:
    def __init__(self,num,name,price,total,last):
        self.__num=int(num)
        self.__name=str(name)
        self.__price=int(price)
        self.__total=int(total)
        self.__last=int(last)
    def display(self):
        print('商品序号:{} 商品名:{} 单价:{} 总数量:{} 剩余数量:{}'.format(self.__num,self.__name,self.__price,self.__total,self.__last),end='\n')
    def income(self):
        return self.__price*(self.__total-self.__last)
    def setdata(self,num,name,price,total,last):
        self.__num = int(num)
        self.__name = str(name)
        self.__price = int(price)
        self.__total = int(total)
        self.__last = int(last)
c=commodity(123,'coke',3,100,50)
c.display()
print(c.income(),end='\n')
c.setdata(124,'water',1,100,50)
c.display()
print(c.income(),end='\n')

