class MyZoo:
    def __init__(self, *args):
        self.animals = args[0] if args else {}
        print('My Zoo!')

    def __repr__(self):
        str1 = '\n'
        for i, j in self.animals.items():
            str1 += f'{i}:{j}\n'
        return str1

    def __eq__(self, other):
        if type(self) == type(other):
            li1 = self.animals.keys()
            li2 = other.animals.keys()
            return li1 == li2

    def __len__(self):
        num = 0
        for i in self.animals.values():
            num += i
        return num
