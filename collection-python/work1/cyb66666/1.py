#输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
a,b,c=input().split()
if a<b:
    temp=a
    a=b
    b=temp
if b<c:
    temp = b
    b = c
    c = temp
if a < b:
    temp = a
    a = b
    b = temp
print(a,b,c)