#创建一个字典（dict），为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典
dict={114:'Lin',514:'Yu',123:'Liu' ,456:'Luo',789:'Zhao'}
ddd = []

for key in dict:
    if key % 2==0:
        ddd.append(key)
for x in ddd:
    del dict[x]

print(dict)
