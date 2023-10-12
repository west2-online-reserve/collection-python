# Author : AnnieHathaway
# 比较x,y,z大小
x = int(input('请输入x'))
y = int(input('请输入y'))
z = int(input('请输入z'))
# 方法1：存列表
lst = [x, y, z]
lst.sort(reverse=True)
print(lst[0], lst[1], lst[2])
# 方法2：抽象的方法
max1 = 0
mid1 = 0
min1 = 0
if x > y:
    max1 = x
else:
    max1 = y
if z > max1:
    max1 = z
else:
    pass
if x < y:
    min1 = x
else:
    min1 = y
if z < min1:
    min1 = z
else:
    pass
if (max1 == x and min1 == y) or (min1 == x and max1 == y):
    mid = z
elif (max1 == z and min1 == y) or (min1 == z and max1 == y):
    mid = x
else:
    mid = y
print(max1, mid, min1)
#方法3：没那么抽象的方法2改良版1.0
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(z, y, x)
#方法4：没那么抽象的方法2改良版2.0
max1 = max(x, y, z)
min1 = min(x, y, z)
if (max1 == x and min1 == y) or (min1 == x and max1 == y):
    mid = z
elif (max1 == z and min1 == y) or (min1 == z and max1 == y):
    mid = x
else:
    mid = y
print(max1, mid, min1)