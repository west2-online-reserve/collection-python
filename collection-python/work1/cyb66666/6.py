#创建一个函数，这个函数可以统计一个只有数字的列表中所有数字的个数，通过字典方式返回
def f(ls):
    dic={}
    for i in ls:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1;
    return dic
ls = [int(i) for i in input().split()]
print(f(ls))
