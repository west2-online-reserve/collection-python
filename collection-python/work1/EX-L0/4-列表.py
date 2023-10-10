#输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
'''
自设输入示例：120 55 win ol fzu 88 fzcu
自设输出示例：[55, 88, 120]
'''
y = []
input_str = input("请有间隔地输入列表：")
x = input_str.split()


for key in x:
    if(key.isdigit()==True):
        y.append(key)

y = [eval(num) for num in y]
y = sorted(y)

print(y)


