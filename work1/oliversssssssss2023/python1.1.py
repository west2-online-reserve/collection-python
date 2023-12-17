x = int(input("请输入一个整数x:"))
y = int(input("请输入一个整数y:"))
z = int(input("请输入一个整数z:"))

numbers = [x,y,z]
new_numbers = sorted(numbers,reverse=True)
for i in new_numbers:
    print(i)