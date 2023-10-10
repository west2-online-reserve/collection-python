for i in range(1, 10):  #从1到9
    for j in range(1, i+1):
        print(str(i) + '*' + str(j) + '=' + str(i * j), end='\t')
    print() 

