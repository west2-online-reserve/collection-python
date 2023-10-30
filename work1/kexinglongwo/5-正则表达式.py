import re
a=input('密码：')
if 6<=len(a)<=18:
    b=re.findall('[A-Za-z]',a)+re.findall('[0-9]',a)
    if len(b)==len(a):
        print('匹配正确')
    else:
        print('只能是数字和英文')
else:
    print('长度只能在6~18')
#github:2877378857qq.com   西二--作业