# 法一：遍历字符串，寻找并替换；(修正版)

# s = input("请输入一个字符串：")
# n = len(s)
# new = ""
# i = 0
# while i < n:
#     if i < n - 1 and s[i:i+2] == "ol":
#         new += "fzu"
#         i += 2  # 跳过'ol'
#     else:
#         new += s[i]
#         i += 1  # 移动到下一个字符
# 
# neww = new[::-1]
# print(neww)

# 法二：利用"str.replace(old,new)方法"
s = input("请输入一个字符串：")
s=s.replace("ol","fzu")
s=s[::-1]
print(s)