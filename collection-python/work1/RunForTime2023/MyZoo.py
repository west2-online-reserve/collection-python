class MyZoo(object):
    animals={}
    def __init__(self,animals={}):
        self.animals=animals
        print("My Zoo!")
    def __str__(self):
        s=""
        for x,y in self.animals.items():
            s=s+x+":"+str(y)+"\n"
        return s
    def __eq__(self, other):
        return self.animals.keys()==other.animals.keys()
    def __len__(self):
        sum=0
        for x in self.animals.values():
            sum+=x
        return sum

a=MyZoo()
a=MyZoo({"pig":5,'dog':6})
b=MyZoo({"pig":1,'dog':1})
print(a,end='')
print(a==b)
print(len(a))