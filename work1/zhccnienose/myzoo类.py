import sys
class MyZoo(object):
    def __init__(self,animals=None):
        self.animal = animals
        print("My Zoo!")
    
    def __str__(self):
        s = ""
        for item in self.animal.items():
            s += str(item[0]) + " : " + str(item[1]) + "\n"
        return s
    
    #输出所有动物总数
    def __len__(self):
        return sum(self.animal.values())
        
    def __eq__(self,other):    
        a1 = self.animal.keys()
        a2 = other.animal.keys()
        
        if(a1&a2 == a1 and a1&a2 == a2):
            return True
        else:
            return False
        
m1 = MyZoo({'pig':5,'sheep':10,'dog':3})
m2 = MyZoo({'pig':10,'sheep':10,'dog':3})
m3 = MyZoo({'dog':1})   

print(len(m1))
print(m1)
print(m1 == m2)
print(m2 == m3)