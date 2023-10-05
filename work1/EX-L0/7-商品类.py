'''
设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。
具有的 公有成员函数是：初始化商品信息的构造函数__init__，显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata
'''
class shop:
    def __init__(self):
        self.__noo=1
        self.__name='I want to join west2-online'
        self.__price=100
        self.__total=0
        self.__last=0
    def display(self):
        print("商品编号：",self.__noo," 商品名称：",self.__name," 商品价格：",self.__price,end=" ")
        print("\n")
    def income(self):
        print("已售出商品的价值是：",self.__price*(self.__total-self.__last))
    def setdata(self,n,na,pr,to,la):
        self.__noo = n
        self.__name = na
        self.__price = pr
        self.__total = to
        self.__last = la

#main函数
n1=input("请输入商品编号：")
n2=input("请输入商品名称：")
n3=int(input("请输入商品价格："))
n4=int(input("请输入商品总数量："))
n5=int(input("请输入商品剩余数量："))

goods=shop()
goods.display()#此步骤用于验证初始化函数是否成功运作
goods.setdata(n1,n2,n3,n4,n5)
goods.display()
goods.income()