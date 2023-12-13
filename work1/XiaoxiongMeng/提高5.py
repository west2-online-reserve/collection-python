import re


email = input("input email")


print(re.match(".*?@.*?\.com", email) is not None)
