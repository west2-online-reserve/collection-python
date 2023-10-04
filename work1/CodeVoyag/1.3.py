num1=input('请输入第一个数,x:')

num2=input('请输入第二个数,y:')

num3=input('请输入第三个数,z:')

if num1>num2:   # if 语句判断
    num1,num2=num1,num2

if num1>num3:
    num1, num3 = num1, num3

if num2>num3:
    num2,num3=num2,num3

print(num1,num2,num3)
