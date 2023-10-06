'''
3.
写一个列表推导式，生成一个5*10的矩阵，矩阵内的所有值为1，再写一个列表推导式，把这个矩阵转置
'''

#转置前的矩阵
lst1=[[1 for i in range(10)] for j in range(5)]
print(lst1)

#转置后的矩阵
lst2=[[lst1[i][j] for i in range(5)] for j in range(10)]
print(lst2)