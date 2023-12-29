class Goods:
    __number = __name = __price = __total = __left = 0

    def __init__(self, number, name, price, total, left):
        self.__number = number
        self.__name = name
        self.__price = price
        self.__total = total
        self.__left = left

    def display(self):
        print(f"number: {self.__number}\nname: {self.__name}\nprice: {self.__price}\ntotal: {self.__total}\nleft: {self.__left}\n")

    def income(self):
        print(self.__price * (self.__total - self.__left))
        print()

    def setdate(self, number, name, price, total, left):
        self.__number = number
        self.__name = name
        self.__price = price
        self.__total = total
        self.__left = left

mygoods = Goods(1010, "name1", 90, 100, 50)
mygoods.display()
mygoods.income()
mygoods.setdate(1011, "name2", 100, 110, 80)
mygoods.display()
mygoods.income()





