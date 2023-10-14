for m in range(1,10):
    for n in range(1,m+1):
        k=m*n
        if m!=n:
            print('%d*%d=%d ' %(n,m,k),end='')
        else:
            print('%d*%d=%d ' %(n,m,k))
