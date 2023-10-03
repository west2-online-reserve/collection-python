'''
5.
写一个正则表达式，用于验证用户密码，长度在6~18 之间，只能包含英文和数字
'''

import re

password=input("请输入你的密码：")

#计算密码长度，传参数进入正则表达式，保证使用match从头开始检查密码的时候可以检查该密码是否全部为英文和数字
Length=len(password)
lst3='[a-zA-Z0-9]{%d}'%(Length if Length>=6 and Length<=18 else -1)

if not(re.match(lst3,password)):
    print("校验失败，密码格式不符合要求，请重新输入")
else:
    print("校验成功，密码格式符合要求")