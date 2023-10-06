# 了解类的魔术方法(Magic Method)。创建类MyZoo，实现以下功能：
#   具有字典anmials，动物名称作为key，动物数量作为value
#   实例化对象的时候，输出"My Zoo!"
#   创建对象的时候可以输入字典进行初始化,若无字典传入，则初始化anmials为空字典
#   print(myzoooo) 输出 动物名称和数量
#   比较两个对象是否相等时，只要动物种类一样，就判断相等：
#   len(myzoooo) 输出所有动物总数

class MyZoo:

    def __init__(self, zooDict):
        # __dict__ 所有类属性组成的字典
        self.__dict__.update(zooDict)
        print("My Zoo!")

    def printDict(self, zooName):
        if self.__dict__ == {}:
            print(f"There is not animal in {zooName}")
        else:
            print(f"{zooName} has: ", end='')
            for animal in list(self.__dict__.keys()):
                print(f"{animal}: {self.__dict__[animal]}", end='  ')
            print()

    def __eq__(self, other):
        listA = list(self.__dict__.keys())
        print(listA)
        listB = list(other.__dict__.keys())
        print(listB)
        if len(listA) == len(listB):
            for animal in listA:
                if animal not in listB:
                    return False
            else:
                return True
        else:
            return False

    def getLen(self):
        totalNum = 0
        for value in list(self.__dict__.values()):
            totalNum += value
        return totalNum


a = MyZoo({"pig": 2, "dog": 3})
b = MyZoo({"monkey": 7})
c = MyZoo({"pig": 3, "dog": 1})
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
a.printDict('a')
b.printDict('b')
c.printDict('c')
print(f"There are {a.getLen()} animals in a")
print(f"There are {b.getLen()} animals in b")
print(f"There are {c.getLen()} animals in c")
print(a == b)
print(a == c)
print(b == c)

