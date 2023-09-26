# num =[int(input("x:")),int(input("y:")),int(input("z:"))]
num = [114514, 23333333333333333, 1919810]


# 当然是选择内置函数啦
def fun1(num):
    return sorted(num, reverse=True)


# 先比前两个
def fun2(num):
    if num[1] > num[0]:
        num = [num[1], num[0], num[2]]
        if num[2] > num[0] > num[1]:
            num = [num[2], num[0], num[1]]
        elif num[0] > num[2] > num[1]:
            num = [num[0], num[2], num[1]]

    return num


# 以及万能的猴子排序
def fun3(num):
    import random

    while not num[0] > num[1] > num[2]:
        random.shuffle(num)  # 随机打乱列表
    return num


print(fun1(num))
print(fun2(num))
print(fun3(num))
