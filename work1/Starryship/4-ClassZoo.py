'''
4.
了解类的魔术方法(Magic Method)。创建类MyZoo，实现以下功能：

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
len(myzoooo) 输出所有动物总数
'''

class MyZoo(object):

    def __init__(self, animals = None):
        '''初始化'''
        if animals==None:
            self.animals={}
        else:
            self.animals=animals
        print("My Zoo!")

    def __str__(self):
        '''输出动物名称和数量'''
        return ",".join(f"{key}的个数为{value}" for key,value in self.animals.items())

    def __eq__(self,other):
        '''比较两个对象'''
        return self.animals.keys()==other.animals.keys()

    def __len__(self):
        '''输出所有动物总数'''
        return sum(self.animals.values())

#举例
myzoooo=MyZoo({'pig':6,'dog':5})
myzoooo2=MyZoo()
myzoooo3=MyZoo({'pig':2,'dog':6})
print(myzoooo)
print(myzoooo==myzoooo3)
print(myzoooo==myzoooo2)
print(len(myzoooo))