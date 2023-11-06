import numpy as np
#使用numpy
# 创建一个5x10的矩阵
matrix = np.ones((5, 10), dtype=int)

# 输出原矩阵的形状和内容
print(f"Original matrix shape: {matrix.shape}")
print(matrix)
print()  # 添加一个空行作为分隔

# 转置矩阵
transposed_matrix = matrix.T

# 输出转置矩阵的形状和内容
print(f"Transposed matrix shape: {transposed_matrix.shape}")
print(transposed_matrix)



#使用列表生成式
matrix = [[1 for _ in range(10)] for _ in range(5)]  # _是一个常用的占位符，表示不关心循环变量的具体值。
# 输出原矩阵的形状
print(f"Original matrix shape: {len(matrix)}x{len(matrix[0])}")
# 输出原矩阵
for row in matrix:
    print(row)

print()  # 添加一个空行作为分隔

transposed_matrix = [[row[i] for row in matrix] for i in range(10)]

# 输出转置矩阵的形状
print(f"Transposed matrix shape: {len(transposed_matrix)}x{len(transposed_matrix[0])}")
# 输出转置矩阵
for row in transposed_matrix:
    print(row)

