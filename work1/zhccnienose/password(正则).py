import re
str1 = input()
pattern = '[a-zA-Z0-9]{6,18}'
if(re.match(pattern,str1)):
    print("valid!")
else:
    print("invalid")