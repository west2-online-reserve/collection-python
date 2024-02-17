# 方法一
m = [int(i) for i in input().split()]
m.sort(reverse = True)
for i in m:
    print(i, end = " ")

# 方法二
a = list(map(int, input().split()))
while len(a):
    m = max(a)
    print(m, end = " ")
    a.remove(m)

# 方法三
a = list(map(int, input().split()))
for i in range(1, 3):
    for j in range(0, 3 - i):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
for i in a:
    print(i, end = " ")

