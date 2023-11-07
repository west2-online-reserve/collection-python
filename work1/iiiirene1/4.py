#4. 输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
lst=list(input("输入元素，并用英文逗号隔开：").split(','))
for item in lst:
    if type(item) == str:
        lst.remove(item)
lst.sort()
print(lst)
