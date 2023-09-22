# p3
def marix_d():
    marix=[[1 for i in range(5)] for i in range(10)]
    in_marix=[[marix[j][i] for j in range(len(marix))] for i  in range (len(marix[0]))]
    print(marix)
    print(in_marix)
# p4
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