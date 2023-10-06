'''了解类的魔术方法(Magic Method)。创建类MyZoo，实现以下功能：

具有字典anmials，动物名称作为key，动物数量作为value

实例化对象的时候，输出"My Zoo!"

创建对象的时候可以输入字典进行初始化,若无字典传入，则初始化anmials为空字典

myzoooo = MyZoo({"pig":5,'dog':6})
myzoooo = MyZoo()
print(myzoooo) 输出 动物名称和数量

比较两个对象是否相等时，只要动物种类一样，就判断相等：

输入：
myzoooo1 = MyZoo({'pig':1})
myzoooo2 = MyZoo({'pig':5})
print(myzoooo1 == myzoooo2)
输出:
My Zoo!
My Zoo!
True
len(myzoooo) 输出所有动物总数'''

class MyZoo():
    def __init__(self, dic=None):
        if dic is None:
            dic = {}
        print("My Zoo!")
        self.dic = dic

    def __str__(self):
        return str(self.dic)

    def __len__(self):
        n = 0
        for value in self.dic.values():
            n+=value
        return n

    def __eq__(self, other):
        keys1=[]
        keys2=[]
        for key in self.dic.keys():
            keys1.append(key)
        for key in other.dic.keys():
            keys2.append(key)
        return sorted(keys1) == sorted(keys2)


