class MyZoo:
    animal = {}
    name = None

    def __init__(self, animals, name):
        print("My Zoo!")
        self.animal = animals
        self.name = name

    def __eq__(self, others):
        rt1 = ''
        rt2 = ''
        for i in self.animal.items():
            rt1 += i[0]
        for i in others.animal.items():
            rt2 += i[0]
        return rt1 == rt2

    def __str__(self):
        rt = ''
        for i in self.animal.items():
            rt += "动物" + i[0] + "有"
            rt += str(i[1]) + "只\n"
        return rt.strip("\n")

    def len(self):
        s = 0
        for i in self.animal.items():
            s += i[1]
        print(s)


myzoooo1 = MyZoo({'pig': 65, 'dog': 99999}, 666)
myzoooo2 = MyZoo({'pig': 65, 'dog': 66}, 777)
print(myzoooo1 == myzoooo2)
print(myzoooo1)
myzoooo1.len()
