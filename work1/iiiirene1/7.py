#7设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。具有的 公有成员函数是：初始化商品信息的构造函数__init__，显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata

class Goods:
    def __init__(self,no,name,price=0,total=0,spare=0):
        self.no = no
        self.name = name
        self.price = int(price)
        self.total = int(total)
        self.spare = int(spare)

class GoodsList:
    def __init__(self):
        self.gdslist = []

    def display(self):
        # 显示信息
        print('{}\t{}\t{}\t{}\t{}\t{}'
              .format('商品序号', '商品名', '单价', '总数量', '剩余数量'))
        for gd in self.gdslist:
            print('{}\t{}\t{}\t{}\t{}'
                  .format(gd.no, gd.name, gd.price, gd.total, gd.spare))

    def setdata(self):
        # 删除信息
        while True:
            no = input('请输入要删除的商品编号:')
            for gd in self.gdslist[::]:
                if gd.no == no:
                    self.gdslist.remove(gd)
                    print('删除成功')
                    break
            else:
                print('该编号不存在')
            choice = input('继续删除(y/n)?').lower()
            if choice == 'n':
                break
    def incomecal(self):
        while True:
            for gd in self.gdslist:
                income = [gd.total - gd.spare]*gd.price
                print(income)


