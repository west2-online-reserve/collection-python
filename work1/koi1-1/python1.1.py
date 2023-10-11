print("x,y,z为三个不同的整数")
x=int(input("请输入第一个整数："))
y=int(input("请输入第二个整数："))
z=int(input("请输入第三个整数："))
#largest=max(x,y,z)
#smallest=min(x,y,z)
#middle=x+y+z-largest-smallest
#print(f"这三个数从大到小的顺序是{largest}，{middle}，{smallest}")
'''numbers=[x,y,z]
numbers.sort(reverse=True)
print(f"这三个数从大到小的顺序是：{numbers}")'''
if x>y and x>z:
    largest=x
    if y>z:
        smallest=z
        middle=y
    else:
        smallest=y
        middle=z
elif y>x and y>z:
    largest=y
    if x>z:
        smallest=z
        middle=x
    else:
        smallest=x
        middle=z
else:
    largest=z
    if x>y:
        smallest=y
        middle=x
    else:
        smallest=x
        middle=y
print(f"这三个数从大到小的顺序是{largest}，{middle}，{smallest}")
