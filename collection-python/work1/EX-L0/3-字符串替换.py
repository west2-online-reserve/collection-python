#输入⼀个字符串，判断字符串中是否含有"ol"这个⼦串，若有把所有的"ol"替换为"fzu"，最后把字符串倒序输出
str = input("请输入字符串:")

str0 = str.replace("ol","fzu")

print(str0[::-1])