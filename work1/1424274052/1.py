#法1：
'''x=int(input('请输入x:'))
y=int(input('请输入y:'))
z=int(input('请输入z:'))
if x<=y:
    (x,y)=(y,x)
if y<=z:
    (y,z)=(z,y)
if x<=y:
    (x,y)=(y,x)
print('三个数由大到小为：%d %d %d' % (x,y,z))'''
#法2：
x=int(input('请输入x:'))
y=int(input('请输入y:'))
z=int(input('请输入z:'))
list=[x,y,z]
list.sort(reverse=True)
print(list)
