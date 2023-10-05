#创建一个函数，这个函数可以统计一个只有数字的列表中所有数字的个数，通过字典方式返回
def f(ls):
    dic={i:len(str(i)) for i in ls if type(i)==int}
    return dic
ls = [int(i) for i in input().split()]
print(f(ls))