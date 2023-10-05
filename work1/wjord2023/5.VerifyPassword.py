import re
content = input("请输入密码：")
if len(content) > 18 or len(content) < 6:
    print("你输入的密码不符合规范！")
else:
    a = re.findall("_",content)
    # 检验密码中是否有_
    if len(a) == 0:
        s1 = re.sub('\w+', '', content)
        # 将字母数字去除观察是否还有其他类型的数据（w+对应数字，字母和_）
        if len(s1) == 0:
            print("你的密码已通过认证！")
        else:
            print("你输入的密码不符合规范！")
    else:
        print("你输入的密码不符合规范！")



