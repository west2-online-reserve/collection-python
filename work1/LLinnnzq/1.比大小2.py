a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if b > a:
    k = a
    a = b
    b = k
if c > a:
    k = a
    a = c
    c = k
if c > b:
    k = b
    b = c
    c = k
print("%d>=%d>=%d" % (a, b, c))



