matrix = [[1 for _ in range(10)] for _ in range(5)]
t_matrix = [[matrix[j][i] for j in range(5)] for i in range(10)]

print("原矩阵：")
for row in matrix:
    print(row)

print("转置后的矩阵：")
for row in t_matrix:
    print(row)
