#输出九九乘法表
i = 1
while i < 10 :
    j = 1

    while j<=i:
       if j==i:
        print(j,"*",i,"=",j*i)

       else:
        print(j, "*", i, "=", j * i, " ",end=" ")
       j = j + 1

    i = i + 1


