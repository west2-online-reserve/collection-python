class MyZoo:
    def __init__(self, input={}) -> None:
        self.anmials = input
        print("My Zoo!")

    def __len__(self):
        return len(self.anmials.keys())
    
    def __str__(self) -> str:
        return "\n".join( "{} have {}".format(name, self.anmials[name]) for name in self.anmials.keys() )
    
    def __eq__(self, other):
        return sorted(self.anmials.keys()) == sorted(other.anmials.keys())
    

myzoooo1 = MyZoo({'pig':1})
myzoooo2 = MyZoo({'pig':5})
print(myzoooo1 == myzoooo2)
print(len(myzoooo1))