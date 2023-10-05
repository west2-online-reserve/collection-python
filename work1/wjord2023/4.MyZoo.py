class MyZoo:

    def __init__(self, dict = None):
        if dict is None:
            self.dict = {}
        else:
            self.dict = dict
        print("My Zoo!")

    def __eq__(self,other):
        list1 = []
        list2 = []
        for key in self.dict.keys():
            list1.append(key)
        for key in other.dict.keys():
            list2.append(key)
        list1 = list1.sort()
        list2 = list2.sort()
        return list1 == list2
    # 将字典中的key提取出来构成列表，再重排列，使得不会因为顺序乱了而判断错误


    def __len__(self):
        return sum(self.dict.values())

    def __str__(self):
        return ",".join([f"{key}:{value}" for key,value in self.dict.items()])

myzoooo = MyZoo({"pig":5,'dog':6})
print(myzoooo)
myzoooo1 = MyZoo({'pig':1})
myzoooo2 = MyZoo({'pig':5})
print(myzoooo1 == myzoooo2)
print(len(myzoooo))


