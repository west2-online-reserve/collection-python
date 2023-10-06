class item:
    def __init__(self, number, name, price, tquan, requan):
        self.number = number
        self.name = name
        self.price = price
        self.tquan = tquan
        self.requan = requan

    def display(self):
        print("""商品序号：%d
         商品名：%s
         单价：%.2f
         总数量：%d
         剩余数量：%d""" % (self.number, self.name, self.price, self.tquan, self.requan))

    def income(self):
        income1 = self.price * (self.tquan - self.requan)
        print('已售出商品价值：%.2f' % (income1))

    def setdata(self):
        change = input('想修改什么？')
        if change == '商品序号':
            self.number = input()
        elif change == '商品名':
            self.name == input()
        elif change == '单价':
            self.price = input()
        elif change == '总数量':
            self.tquan = input()
        elif change == '剩余数量':
            self.requan = input()
        else:
            print('无此项')

a = item(1, '铅笔', 2.5, 100, 27)
b = item(2, '钢笔', 8, 60,38)
c = item(3, '中性笔', 6.8, 150, 33)
d = item(4, '圆珠笔', 4.8, 80, 12)
e = item(5, '荧光笔', 8, 80, 9)
c.display()
a.income()
e.setdata()




