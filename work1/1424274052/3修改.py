str1=str(input('请输入一个字符串：'))
if 'ol' in str1:
    str2=str1.replace('ol','fzu')
    print('该字符串存在‘ol’这个子串')
    print(str2[::-1])
else:
    print('该字符串不存在‘ol’这个子串')




