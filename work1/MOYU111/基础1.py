a=eval(input("a="))
b=eval(input("b="))
c=eval(input("c="))


if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b



print(a,b,c)