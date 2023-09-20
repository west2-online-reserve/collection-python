class Goods:
    def __init__(self,ord,name,price,alnum,lsnum):
        self.__ord=ord
        self.__name=name
        self.__price=price
        self.__alnum=alnum
        self.__lsnum=lsnum
    def display(self):
        print(f'商品序号： {self.__ord} ')
        print(f'商品名： {self.__name} ')
        print(f'单价： {self.__price} ')
        print(f'总数量： {self.__alnum} ')
        print(f'剩余数量： {self.__lsnum} ')
    def income(self):
        return self.__price * (self.__alnum - self.__lsnum)
    def setdata(self,ord,name,price,alnum,lsnum):
        self.__ord=ord
        self.__name=name
        self.__price=price
        self.__alnum=alnum
        self.__lsnum=lsnum
        
# item = Goods(29,'llalala',5,888,8)
# item.display()

# 使用示例
item = Goods(1, "lalalal", 8, 99999, 888)
item.display()
print(f"已售出商品价值: {item.income()}")

# 修改商品信息
item.setdata("平板电脑", 800, 150, 75,8)
item.display()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        