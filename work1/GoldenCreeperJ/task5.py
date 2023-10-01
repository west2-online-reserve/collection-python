import re

string = '[a-zA-Z0-9]{6,18}$'
password = input()
if re.match(string, password):
    print('Success')
else:
    print('Fail')

