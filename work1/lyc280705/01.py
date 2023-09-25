#方法1
X=int(input())
Y=int(input())
Z=int(input())
if X<Y:
    if Y<Z:
        print(Z,Y,X)
    else:
        if X>Z:
            print(Y,X,Z)
        else:
            print(Y,Z,X)
else:
    if Y<Z:
        if X>Z:
            print(X,Z,Y)
        else:
            print(Z,X,Y)
    else:
        print(X,Y,Z)

#方法2
numbers = []
for i in range(3):
    numbers.append(int(input()))
numbers.sort(reverse=True)
for j in numbers:
    print(j,end=" ")