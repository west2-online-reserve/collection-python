class goods:
    __number=0
    __name=''
    __price=0
    __gross=0
    __surplus=0
    def __init__(self,num,n,p,g,s):
        self.__number=num
        self.__name=n
        self.__price=p
        self.__gross=g
        self.__surplus=s
    def display(self):
        print('商品序号:%d 商品名:%s 单价：%d 总数量：%d 剩余数量:%d'%(self.__number,self.__name,self.__price,self.__gross,self.__surplus))
    def income(self):
        m=0
        m=self.__price*(self.__gross-self.__surplus)
        print('已售出商品价值：%d'%m)
    def setdate(self,num,n,p,g,s):
        self.__xuhao=num
        self.__name=n
        self.__price=p
        self.__gross=g
        self.__surplus=s
        print('修改后的商品信息为：商品序号:%d 商品名:%s 单价：%d 总数量：%d 剩余数量:%d' %(self.__number,self.__name,self.__price,self.__gross,self.__surplus))
x=goods(12,'玩具',15,100,20)
x.display()
x.income()
x.setdate(13,'文具',10,80,10)
        

