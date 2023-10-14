# Author : AnnieHathaway
lst = input('请输入一个列表: ').split(',')
new_lst = []
for i in lst:
    try:
        num = int(i.strip())
        new_lst.append(num)
    except ValueError:
        # 跳过该元素
        pass
new_lst.sort()
print("排序后的整数列表:", new_lst)
