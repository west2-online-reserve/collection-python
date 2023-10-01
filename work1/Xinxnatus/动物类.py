class MyZoo:
    def __init__(self,animals=None):
        if animals is None:
            self.animals = {}
        else:
            self.animals = animals
        print("My Zoo!")

    def __eq__(self,zoo2):
        return self.animals.keys() == zoo2.animals.keys()

    def __len__(self):
        return sum(self.animals.values())

    def __str__(self):
        return ",".join([f"{animal}:{count}" for animal, count in self.animals.items()])


myzoooo1 = MyZoo({'pig':1})
myzoooo2 = MyZoo({'pig':5})
myzoooo3 = MyZoo()
myzoooo = MyZoo({"pig":5,'dog':6})
print(myzoooo1==myzoooo2)
print(len(myzoooo))
print(myzoooo)
