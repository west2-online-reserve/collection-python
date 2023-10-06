class item(object):
    def __init__(self, id, name, price, number, remain):
        self.id = id
        self.name = name
        self.price = price
        self.number = number
        self.remain = remain

    def display(self):
        print("商品序号: " + str(self.id))
        print("商品名: " + self.name)
        print("单价: " + str(self.price))
        print("总数量: " + str(self.number))
        print("剩余数量: " + str(self.remain))

    def income(self):
        print("已售出的商品价值为 " + str(self.price * (self.number - self.remain)))

    def setdata(self):
        self.id = int(input("商品序号:"))
        self.name = input("商品名:")
        self.price = int(input("单价:"))
        self.number = int(input("总数量:"))
        self.remain = int(input("剩余数量:"))

    pass


product = item(10001, "苹果", 3, 100, 50)
product.display()
product.income()
product.setdata()
product.display()
product.income()