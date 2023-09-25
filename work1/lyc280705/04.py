list = input("输入一个列表：").split(",")
list = [int(x) for x in list if x.isdigit()]#完全不知道有isdigit这个函数
list = sorted(list)
print(list)