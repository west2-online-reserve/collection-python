a=str(input())
print(a.count("ol"))
b=a.count("ol")
if b!=0:
    print("该字符串中含有'ol'子串")
    c=a.replace("ol","fzu")
    print(c[::-1])
else:
    print("该字符串中不含有'ol'子串")
