class MyZoo:
    def __init__(self,anmials={}):
        self.anmials=anmials
        print("My Zoo")
    def __eq__(self, other):
        if self.anmials.keys()==other.anmials.keys():
            return True
        else:
            return False

    def __str__(self) :
        t=''
        for i,o in self.anmials.items():
            t=t+(f"动物种类有:{i}  动物数量为：{o}")+'\n'
        return t

    def __len__(self):
        t =0
        for i, o in self.anmials.items():
            t+=o
        return t
a=MyZoo({'dog':2,"pig":1})
b=MyZoo({"pig":1,'dog':2})
print(a==b)
print(a.__str__())
print(a.__len__())
#github:2877378857qq.com   西二--作业
