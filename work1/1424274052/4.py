import re
list1=list(input('请输入一个列表：'))
list1.sort()
string1=str(list1)
n=[int(re.sub("\D","",string1))]
string2=str(n)
list2=list(string2)
list2.remove('[')
list2.remove(']')
print(list2)