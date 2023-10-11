'''写一个正则表达式，用于验证用户密码，长度在6~18 之间，只能包含英文和数字'''
import re
a = input('输入密码：')
pattern = r'[a-zA-Z1-9]+'
matches = re.sub(pattern,'',a)
if (not matches) | 6<=len(a)<=18:
    print('合格')
else:
    print('不合格')
