
list1=eval(input('请输入一个列表：'))
list2=[]
list3=[]
for i in list1:
    if type(i) == str:
        list2.append(i)
for i in list1:
    if i not in list2:
        list3.append(i)
list3.sort()
print(list3)