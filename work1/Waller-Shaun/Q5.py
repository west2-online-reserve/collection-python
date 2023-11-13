'''写一个正则表达式，用于验证用户密码，长度在6~18 之间，只能包含英文和数字'''
import re
a = input('密码')
pattern = r'[a-zA-Z0-9]{6,18}'
matches = re.sub(pattern,'',a)
if not matches:
    print('合格')
else:
    print('不合格')
