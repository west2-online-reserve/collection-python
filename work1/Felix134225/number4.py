lis=input('请输入一个只含有整数或者字符串的列表（用空格键分隔元素）：')
lis=lis.split()
lis2=[]
for item in lis:
    if item.isdigit():
        lis2.append(int(item))
lis2.sort(reverse=False)
print(lis2)