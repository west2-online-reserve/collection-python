x = int(input("请输入第一个整数x: "))
y = int(input("请输入第二个整数y: "))
z = int(input("请输入第三个整数z: "))

if x >= y and x >= z:
    if y >= z:
        print(x, y, z)
    else:
        print(x, z, y)
elif y >= x and y >= z:
    if x >= z:
        print(y, x, z)
    else:
        print(y, z, x)
else:
    if x >= y:
        print(z, x, y)
    else:
        print(z, y, x)