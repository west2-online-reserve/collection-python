dict1 = {102314211: '王德发', 102314212:'骆斌', 102314213:'狄仁杰',102314214:'李元芳'}
for k in list(dict1.keys()):
    n=k%10
    if n%2==0:
        del dict1[k]
print(dict1)