# 方式一：

i=1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%d"%(i,j,i*j),end=' ')
        j+=1
        pass
    print(" ")
    i+=1
    pass

# 方式二：

i=9
while i>=1:
    j=1
    while j<=i:
        print("%d*%d=%d"%(j,i,j*i),end=" ")
        j+=1
        pass
    print(" ")
    i-=1
    pass
