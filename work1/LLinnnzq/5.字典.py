d = {}
d[111] = '张三'
d[112] = '李四'
d[113] = '王五'
d[114] = '小赵'
d[115] = '张飞'
d[116] = '李明'
for i in list(d.keys()):
    if i % 2 == 0:
        del d[i]
print(d)