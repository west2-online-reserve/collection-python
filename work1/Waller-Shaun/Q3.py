'''写一个列表推导式，生成一个5*10的矩阵，矩阵内的所有值为1，再写一个列表推导式，把这个矩阵转置'''
lst1 = [[1 for i in range(10)]for o in range(5)]
print(lst1)
lst2 = [[lst1[0][0] for i in range(len(lst1))] for o in range(len(lst1[0]))]
print(lst2)