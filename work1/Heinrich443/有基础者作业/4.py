class MyZoo:
    animals = {}

    def __init__(self, dic):
        print("My Zoo!")
        self.animals = dic

    def __eq__(self, other):
        z1 = set(self.animals.keys())
        z2 = set(other.animals.keys())
        if z1 == z2:
            return True
        return False

    def __len__(self):
        res = 0
        for key in self.animals.keys():
            res += int(self.animals[key])
        return res


zoo1 = MyZoo({"pig": 1, "dog": 5, "cat": 3})
zoo2 = MyZoo({"cat": 9, "panda": 4, "pig": 2})
print(zoo1 == zoo2)
print(len(zoo1))
print(len(zoo2))