lst = input("请输入一个列表（用空格分隔元素）：")
lst = lst.split()

new_lst = []
for item in lst:
     if item.isdigit():  # 检查字符串是否可以转换为整数
        new_lst.append(int(item))

sorted_lst = sorted(new_lst)

print(sorted_lst)