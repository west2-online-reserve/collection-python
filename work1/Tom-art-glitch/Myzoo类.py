class Myzoo(object):
    def __init__(self,d):
        if len(d)==0:
            self.animals={}
        else:
            self.animals=d
        print("My zoo!")
    def print(self):
        for i in self.animals:
            print(i+':',self.animals[i])

    def __eq__(self, other):
        return self.animals.keys()==other.animals.keys()
    def len(self):
        s=0
        for i in self.animals:
            s+=self.animals[i]
        print(s)
myzoo1 = Myzoo({'pig':1})
myzoo2 = Myzoo({'pig':5})
print(myzoo1==myzoo2)
myzoo1.print()
myzoo2.len()


