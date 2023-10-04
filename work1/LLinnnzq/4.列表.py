l = eval(input('输入一个含有整数和字符串的列表'))
n = len(l)
d = []
for i in range(n):
    if type(l[i]) == str:
        d.append(i)
l = [l[i] for i in range(n) if (i not in d)]
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            k = l[i]
            l[i] = l[j]
            l[j] = k
print(l)