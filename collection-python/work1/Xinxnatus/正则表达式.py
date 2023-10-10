import re


def check(password):
    return bool(re.match(r'^[a-zA-Z0-9]{6,18}$',password))


p1 = 'avfe22LLL'
p2 = '484182sdwa'
p3 = 'a'
p4 = '123dawdfaefawffaffwa'
p5 = '123456!'

for i in [p1,p2,p3,p4,p5]:
    if check(i) == 1:
        print("密码格式正确！")
    else:
        print("密码格式错误！")