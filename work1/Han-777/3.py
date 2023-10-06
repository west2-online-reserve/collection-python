# 写一个列表推导式，生成一个5*10的矩阵，矩阵内的所有值为1，再写一个列表推导式，把这个矩阵转置
matrix_S = [[1 for i in range(10)] for j in range(5)]
print(matrix_S)


matrix_Transpose = [[row[i] for row in matrix_S] for i in range(10)]
print(matrix_Transpose)
