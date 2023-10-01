def p1():
    a=int(input(" 请依次输入三个数"))
    b=int(input())
    c=int(input())
    if a>b:
        a,b=b,a
    if a>c:
        a,c=c,a
    if b>c:
        b,c=c,b
    print(a, b, c)
# p1()
    
def p2():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"\t{j}*{i}={i*j}",end="")
        print('')
def p3():
    a=input("输入一个字符串")
    b=0
    if "ol" in a:
        a1=a.replace("ol","fzu")
        print(f"ol is in {a}")
    a1=a1[::-1]
    print(a1)
def p4():
    a=eval(input("输入一个列表:"))
    b=[]
    for i in a:
        if type(i) ==int:
            b.append(int(i))
    b.sort()
    print(b)
    
def p5():
    dict1={10231:"jack",10232:"john",10233:"ljj",10234:"zjl"}
    print(dict1)
    dict2={}
    for i in dict1:
        if i%2==1:
            dict2[i]=dict1[i]
    print(dict2)
def p6(list):
    set ={}
    for i in range(len(list)):
        if list[i] not in set:
            set[list[i]]=1
        else: set[list[i]]+=1
    return set
class Goods:
    def __init__(self) -> None:
        pass
    __Name = "Sras"
    __Number = 10086
    __Unit_price = 10
    __Amount=1000
    __Leave=200
    def display(self):
        print("成品名:\t",self.__Name)
        print("编号:\t",self.__Number)
        print("单价:\t",self.__Unit_price)
        print("总量:\t",self.__Amount)
        print("剩余量:\t",self.__Leave)
    def income(self):
        t=(self.__Amount-self.__Leave)*self.__Unit_price
        print(f"售出的商品总价为:{t}")
    def setdata(self,name,number,unit_price,amount,leave):
        self.__Name=name
        self.__Number=number
        self.__Unit_price=unit_price
        self.__Amount=amount
        self.__Leave=leave


