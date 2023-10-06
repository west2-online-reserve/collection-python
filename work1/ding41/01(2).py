x=int(input("输入第一个整数"))
y=int(input("输入第二个整数"))
z=int(input("输入第三个整数"))
m=[x,y,z]
if x==max(m):
    if y==min(m):
        print(x,z,y)
    else:
        print(x,y,z)
elif y==max(m):
    if x==min(m):
        print(y,z,x)
    else:
        print(y,x,z)
else :
    if x==min(m):
        print(z,y,x)
    else:
        print(z,x,y)