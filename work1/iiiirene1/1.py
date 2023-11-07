#输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
x = int(input('第一个整数x：'))
y = int(input('第二个整数x：'))
z = int(input('第三个整数x：'))
# f方法1
max = x
if y > x:
    if y > z:
        max = y
        y = x
        x = max
        if z > y:
            max = z
            z = y
            y = max
    elif z > y:
        max = z
        z = x
        x = max
else:
    if z > x:
        max = z
        z = x
        x = max
        if z > y:
            max = z
            z = y
            y = max
    else:
        if z > y:
            max = z
            z = y
            y = max
print(x, y, z)

# 方法2
if y > x:
    if z > y:
        z, x = x, z
    else:
        if x > z:
            y, x = x, y
        else:
            x, y, z = y, z, x
else:
    if z > x:
        x, y, z = z, x, y
    else:
        if z > y:
            z, y = y, z
print(x, y, z)


# 方法3
if y > x:
    x, y = y, x
if z > x:
    x, z = z, x
if z > y:
    y, z = z, y

print(x, y, z)

#方法4
List = [x, y, z]
List = sorted(List,reverse=True) #sorted可实现对可迭代对象进行排序，其中reverse参数默认为False，实现由小到大排序，此处需要实现由大到小排序，故需把此参数值赋值为True
print(List)
