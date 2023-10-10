#法一：利用条件语句硬找；
# x=int(input("请输入整数x："))
# y=int(input("请输入整数y："))
# z=int(input("请输入整数z："))
# min=x
# max=x
# if min > y:
#     min=y
# if min > z:
#     min=z
# if max < y:
#     max=y
# if max < z:
#     max=z
# mid=x+y+z-max-min
# print(f"x,y,z从大到小依次是：{max} {mid} {min}")

# 法二：利用函数；
# x=int(input("请输入整数x："))
# y=int(input("请输入整数y："))
# z=int(input("请输入整数z："))
# maxi=max(x,y,z)
# mini=min(x,y,z)
# midi=x+y+z-maxi-mini
# print(f"x,y,z从大到小依次是：{maxi} {midi} {mini}")

# 法三：先比较两个，后衍射至三个；
# x = int(input("请输入整数x："))
# y = int(input("请输入整数y："))
# z = int(input("请输入整数z："))
# 
# if x > y:
#     if y > z:
#         print(f"x, y, z从大到小依次是{x} {y} {z}")
#     elif y < z and z < x:
#         print(f"x, y, z从大到小依次是{x} {z} {y}")
#     else:
#         print(f"x, y, z从大到小依次是{z} {x} {y}")
# else:#y>x 
#     if x > z:
#         print(f"x,y,z从大到小依次是{y} {x} {z}")
#     elif y > z and z > x :
#         print(f"x,y,z从大到小依次是{y} {z} {x}")
#     else:
#         print(f"x,y,z从大到小依次是{z} {y} {x}")

# 法四 : 利用sort()函数
# x=int(input("请输入整数x："))
# y=int(input("请输入整数y："))
# z=int(input("请输入整数z："))
# listt = [x,y,z]
# listt.sort(reverse = True)#reverse=True表示降序
# for i in listt:
#     print(str(i))

    