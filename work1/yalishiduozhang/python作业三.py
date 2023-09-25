list1 = [[1 for i in range(10)] for j in range(5)]
list2 = [[list1[j][i] for j in range(5)] for i in range(10)]
print('原始矩阵：')
for row in list1:
    print(row)
print('转置矩阵')
for row in list2:
    print(row)