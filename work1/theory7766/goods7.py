class Goods(object):
    # 限定Person对象属性
    __slots__ = ('_num','_name','_price','_total','_remain')

    def __init__(self,num,name, price,total,remain):
        self._num = num
        self._name = name
        self._price = price
        self._total = total
        self._remain = remain

    def display(self):
        print('商品序号：',self._num, '商品名：', self._name,'单价：',
              self._price, '总数量：', self._total, '剩余数量：', self._remain)

    def income(self):
        return self._price*(self._total-self._remain)

    def setdata(self, num, name, price, total, remain):
        self._num = num
        self._name = name
        self._price = price
        self._total = total
        self._remain = remain

def main():
    good1 = Goods(1001,'棉花糖', 2, 15, 5)
    good1.display()
    print('收入：', good1.income())
    good1.setdata(1001, '爆米花', 5, 100, 90)
    good1.display()
    print('收入：', good1.income())

if __name__=='__main__':
    main()
