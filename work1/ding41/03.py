str=input("输入一个字符串")
if "ol" in str:
    str=str.replace("ol","fzu")
    print("".join(reversed(str)))
else:
    print("该字符串不包含'ol'")