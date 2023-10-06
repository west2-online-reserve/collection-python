class MyZoo:
    def __init__(self,anmials={}):
        self.anmials=anmials
        print("My Zoo")
    def __eq__(self, other):
        if self.anmials.keys()==other.anmials.keys():
            return True
        else:
            return False
a=MyZoo({'dog':2,"pig":1})
b=MyZoo({"pig":1,'dog':2})
print(a==b)
#github:2877378857qq.com   西二--作业
