l = list(input("输入一个列表:(其中的元素用空格分隔)").split())
res = []
for it in l:
    if it.isdigit():
        res.append(int(it))
res.sort()
print(res)