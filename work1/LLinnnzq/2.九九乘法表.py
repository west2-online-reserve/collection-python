for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            num = i*j
            print(str(j)+'*'+str(i)+'='+str(num))
    print()

