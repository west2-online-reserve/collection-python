import re
content = input("请输入密码：")
r = re.match(r"^[a-zA-Z0-9]{6,18}$",content)
if r:
    print("密码已通过验证")
else:
    print("密码不符合规范")


