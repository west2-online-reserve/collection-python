import re

password = input("请输入密码：")
pattern = r'^[0-9a-zA-Z]{6,18}$'   # 正则表达式

if re.match(pattern, password):
    print("密码可用！")
else:
    print("密码不可用！")
