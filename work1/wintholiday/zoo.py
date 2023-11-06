class MyZoo:
    def __init__(self, animals=None):
        self.animals = animals or {}
        print("My Zoo!")

    def __str__(self):
        return "\n".join([f"{k}: {v}" for k, v in self.animals.items()])

    def __eq__(self, other):
        return set(self.animals.keys()) == set(other.animals.keys())

    def __len__(self):
        return sum(self.animals.values())

myzoooo1 = MyZoo({"pig": 5, "dog": 6})
print(myzoooo1)

myzoooo2 = MyZoo()
print(myzoooo2)

myzoooo3 = MyZoo({'pig': 1})
myzoooo4 = MyZoo({'pig': 5})
print(myzoooo3 == myzoooo4)

print(len(myzoooo1))
print(len(myzoooo2))
print(len(myzoooo3))
print(len(myzoooo4))
