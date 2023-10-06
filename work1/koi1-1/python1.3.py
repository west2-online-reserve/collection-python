input_str = input("请输入一个字符串：")
if "ol" in input_str:
    new_str = input_str.replace("ol", "fzu")
else:
    new_str = input_str
reversed_str = new_str[::-1]
print(f"处理后的字符串：{reversed_str}")
