import sys
class MyZoo(object):
    def __init__(self,dic):
        self.animal = dic
        self.sum = 0
        print("My Zoo!")
        
    def __eq__(self,other):    
        a1 = self.animal.keys()
        a2 = other.animal.keys()
        
        if(a1&a2 == a1 and a1&a2 == a2):
            return True
        else:
            return False

def print(a):
    if(isinstance(a,MyZoo)):
        for item in a.animal:
            sys.stdout.write(str(item.key()))
            sys.stdout.write(" : ")
            sys.stdout.write(str(item.value()))
            sys.stdout.write("\n")
    else:
        sys.stdout.write(str(a))
        sys.stdout.write("\n")

#输出所有动物总数
def len(self):
    self.sum = 0
    a_val = self.animal.values()
    for i in a_val:
        self.sum += i
    print(self.sum)
        
m1 = MyZoo({'pig':5,'sheep':10,'dog':3})
m2 = MyZoo({'pig':10,'sheep':10,'dog':3})
m3 = MyZoo({'dog':1})   

len(m1)
#print(m1)
print(m1 == m2)
print(m2 == m3)