import re
str1 = input()
pattern = r'^[a-zA-Z0-9]{6,18}$'
if(re.match(pattern,str1)):
    print("yes")
else:
    print("no")