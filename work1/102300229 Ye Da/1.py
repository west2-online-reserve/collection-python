class myZoo:
    def __init__(self,animals=None):
        if animals==None:
            self.animals={}
        else:
            self.animals=animals
    def __str__(self):
        return str(self.animals)
    def __eq__(self,other):
         return self.animals.keys() == other.animals.keys()
    def __len__(self):
        return sum(self.animals.values())
    
    
    
        
myzoooo1 = myZoo({'pig':1})
myzoooo2 = myZoo({'pig':5,'duck':2})
print(myzoooo1 == myzoooo2)
print(len(myzoooo2))
print(myzoooo2)