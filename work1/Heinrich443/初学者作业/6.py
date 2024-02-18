def mycount(mylist):
    d = {}
    for it in mylist:
        if it in d:
            d[it] += 1
        else:
            d[it] = 1
    return d

l = list(map(int, input("输入一个只含数字的列表：（数字间用空格分隔）").split()))
res = mycount(l)
print(res)