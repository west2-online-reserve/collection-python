class goods:
    __xuhao=0
    __name=''
    __price=0
    __zong=0
    __sheng=0
    def __init__(self,x,n,p,z,s):
        self.__xuhao=x
        self.__name=n
        self.__price=p
        self.__zong=z
        self.__sheng=s
    def display(self):
        print('商品序号:%d 商品名:%s 单价：%d 总数量：%d 剩余数量:%d'%(self.__xuhao,self.__name,self.__price,self.__zong,self.__sheng))
    def income(self):
        m=0
        m=self.__price*(self.__zong-self.__sheng)
        print('已售出商品价值：%d'%m)
    def setdate(self,x,n,p,z,s):
        self.__xuhao=x
        self.__name=n
        self.__price=p
        self.__zong=z
        self.__sheng=s
        print('修改后的商品信息为：商品序号:%d 商品名:%s 单价：%d 总数量：%d 剩余数量:%d' %(self.__xuhao,self.__name,self.__price,self.__zong,self.__sheng))
x=goods(12,'玩具',15,100,20)
x.display()
x.income()
x.setdate(13,'文具',10,80,10)
        

