class Myzoo():
    def __init__(self,animals = None):
        if animals == None:
            self.animals = {}
        else:
            self.animals = animals
        print('My Zoo!')
    def __str__(self):
        return '\n'.join(f'{animal} : {count}' for animal,count in self.animals.items())
    def __eq__(self,other):
        return set(self.animals.keys()) == set(other.animals.keys())
    def __len__(self):
        return sum(self.animals.values())
myzoooo=Myzoo({'pig':5,'dog':6})
myzoooo
print(myzoooo)
myzoooo1 = Myzoo({'pig':1})
myzoooo2 = Myzoo({'pig':5})
print(myzoooo1 == myzoooo2)
print(len(myzoooo1))









