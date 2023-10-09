matrix = [[i for i in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] for i in [1, 1, 1, 1, 1]]
print("转置前：",matrix)
new_matrix = [[row[i] for row in matrix] for i in range(5)]
print("转置后：",new_matrix)