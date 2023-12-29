s = input()
if s.find("ol") != -1:
    print('含有“ol"子串')
    s = s.replace("ol", "fzu")
else:
    print('不含有"ol"子串')
print(s[::-1])
# 输出也可以用下面的写法：
# print("".join(reversed(s)))

