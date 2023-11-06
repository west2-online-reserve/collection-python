x = float(input("输入整数x:"))
y = float(input("输入整数y:"))
z = float(input("输入整数z:"))
if x >= y >= z:
    print("x,y,z")
elif x >= z >= y:
    print("x,z,y")
elif y >= z >= x:
    print("y,z,x")
elif y >= x >= z:
    print("y,x,z")
elif z >= x >= y:
    print("z,x,y")
elif z >= y >= x:
    print("z,y,x")