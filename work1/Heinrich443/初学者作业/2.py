# 方法一
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j: < 2} ', end = " ")
    print()

# 方法二
print('\n'.join([' '.join([f'{i} * {j} = {i * j: < 3} ' for j in range(1, i + 1)]) for i in range(1, 10)]))

