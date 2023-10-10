def produce():
    a = [[1 for i in range(10)] for j in range(5)]
    return a


def transpose(matrix):
    t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return t_matrix


a = produce()
for i in a:
    print(*i, sep=' ')
print('')

b = transpose(a)
for j in b:
    print(*j,sep=' ')