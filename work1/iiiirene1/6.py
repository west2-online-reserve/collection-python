#创建一个函数，这个函数可以统计一个只有数字的列表中各个数字出现的次数，通过字典方式返回


l1= map(float, input("输入数字元素，并用,隔开：").split(','))
dict = {}
for i in l1:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)