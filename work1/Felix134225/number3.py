word=str(input('请输入一个字符串：'))
if 'ol' in word:
    word=str.replace(word,'ol','Fzu')
print(word[::-1])