import random
list = [[1 for i in range(5)] for j in range(10)]
for i in range(len(list)):
    print(list[i])
lst=[[list[i][j] for i in range(len(list))]for j in range(len(list[0]))]
for i in range(len(lst)):
    print(lst[i])