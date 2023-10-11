list1 = input("请输入一个包含字符串和整数的列表，用逗号分隔：").split(",")
list2 = []
for i in list1:
    try:
        num = int(i)
        list2.append(i)
    except ValueError:
        pass
sorted_list = sorted(list2)
print(sorted_list)

