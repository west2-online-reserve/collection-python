class MyZoo:
    number=0
    species=[]
    def __init__(self,animal={}):
        for key in self.animal:
            if key not in self.species:
                self.species.append(key)
            self.number+=animal[key]
        print("My Zoo！") 

    def __eq__(self, other) -> bool:
        return self.species ==other.species
    # def __str__(self) -> str:

    def __str__(self) -> str:
        return  f"动物种类有:{self.species}  动物数量为：{self.number}"
    
    def __len__(self):
        return self.number