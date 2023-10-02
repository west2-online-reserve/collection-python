class item(object):
    def __init__(self, id, name, price, number, remain):
        self.id = id
        self.name = name
        self.price = price
        self.number = number
        self.remain = remain

    def display(self):
        print("ID: " + str(self.id))
        print("Name: " + self.name)
        print("Price: " + str(self.price))
        print("Number: " + str(self.number))
        print("Remaining: " + str(self.remain))

    def income(self):
        print("Income: " + str(self.price * (self.number - self.remain)))

    def setdata(self):
        self.id = int(input("id:"))
        self.name = input("name:")
        self.price = int(input("price:"))
        self.number = int(input("number:"))
        self.remain = int(input("remain:"))

    pass


baicai = item(1, "baicai", 10, 100, 50)
baicai.display()
baicai.income()
baicai.setdata()
baicai.display()
