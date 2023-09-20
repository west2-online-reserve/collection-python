# 法一：遍历字符串，寻找并替换；
# s = input("请输入一个字符串：")
# n=len(s)
# new=""
# for i in range(n-1):
#     if s[i:i+2]=="ol":
#         new+="fzu"
#     else:
#         new+=s[i:i+2]
# neww=new[::-1]
# print(neww)

# 法二：利用"str.replace(old,new)方法"
# s = input("请输入一个字符串：")
# s=s.replace("ol","fzu")
# s=s[::-1]
# print(s)