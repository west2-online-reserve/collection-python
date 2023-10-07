str = input("请输入一个字符串: ")
if "ol" in str:
    str = str.replace("ol", "fzu")
print(str[::-1])