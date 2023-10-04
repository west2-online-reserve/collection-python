def Countnum(L):
    number = len(L)
    di = {'这个列表中数字的个数':number}
    return (di)

yourlist = eval(input('输入一个只有数字的列表'))
print(Countnum(yourlist))



