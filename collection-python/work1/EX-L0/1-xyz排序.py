#输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出

a = int(input("输入第一个数字:"))
b = int(input("输入第二个数字:"))
c = int(input("输入第三个数字:"))

List = [a,b,c]

#第一种：利用现有函数排序
List = sorted(List,reverse=True)
for x in List:
    print(x,end=" ")
#第二种：一个一个比较排序
'''
if a>b and a>c:
   if b>c:
      print(a,b,c)
   else:
      print(a,c,b)
elif b>a and b>c:
    if a>c:
      print(b,a,c)
    else:
      print(b,c,a)
elif c>a and c>b:
    if b>a:
      print(c,b,a)
    else:
      print(c,a,b)
'''