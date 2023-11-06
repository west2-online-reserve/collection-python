#[法一]：
x=int(input('请输入整数x：'))
y=int(input('请输入整数y：'))
z=int(input('请输入整数z：'))
number=[x,y,z]
for i in range(0,len(number)-1):
    for j in range(i+1,len(number)):
        if number[i]<number[j]:
            number[i],number[j]=number[j],number[i]
print(number)
#[法二]：
x=int(input('请输入整数x：'))
y=int(input('请输入整数y：'))
z=int(input('请输入整数z：'))
list=[x,y,z]
list.sort(reverse=True)
print(list)
#[法三]：
x=int(input('请输入整数x：'))
y=int(input('请输入整数y：'))
z=int(input('请输入整数z：'))
number=[x,y,z]
for i in range(0,len(number)-1):
    for j in range(i,len(number)-1):
        if number[j]<number[j+1]:
            number[j],number[j+1]=number[j+1],number[j]
print(number)