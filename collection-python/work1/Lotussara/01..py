# 方法一：

x=int(input())
y=int(input())
z=int(input())
max=x
if y>max:
    max=y
    pass
if z>max:
    z=max
    pass
min=y
if x<min:
    min=x
    pass
if z<min:
    min=z
    pass
media=z
if x<max and x>min:
    media=z
    pass
if y<max and y>min:
    media=y
    pass
print("%d %d %d"%(max,media,min))

# 方法二：
x=int(input())
y=int(input())
z=int(input())
if x>y and y>z:
    print("%d %d %d"%(x,y,z))
elif x>z and z>y:
    print('%d %d %d'%(x,z,y))
elif y>x and x>z:
    print('%d %d %d'%(y,x,z))
elif y>z and z>x:
    print('%d %d %d'%(y,z,x))
elif z>x and x>y:
    print("%d %d %d"%(z,x,y))
elif z>y and y>x:
    print("%d %d %d"%(z,y,x) )
    pass
