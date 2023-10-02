class Commodity:
    def __init__(self,cid,cname,total=0,rest=0,price=0) :
        self.__cid=cid
        self.__cname=cname
        self.__total=total
        self.__rest=rest
        self.__price=price
    def display(self):
        
        print(self.__cid,end=",")
        print(self.__cname,end=",")
        print(self.__total,end=",")
        print(self.__rest,end=",")
        print(self.__price)
        
    def buy(self,num):
        self.rest=self.__rest-num
    def calculate(self):
        print("已经售出",self.__price*(self.__total-self.__rest),"元")
        return  self.__price*(self.__total-self.rest)
        
    def setdata(self,id,name,sum,rest,price):
        self.__cid=id
        self.__cname=name
        self.__total=sum
        self.__rest=rest
        self.__price=price

l1=Commodity(cid=1,cname="汉堡",total=1,rest=1,price=15)
l1.display()
l1.buy(1)
l1.display()
l1.calculate()
l1.setdata(id=3,name="burger",sum=0,rest=0,price=15)
l1.display()


