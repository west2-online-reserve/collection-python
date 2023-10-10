a=[[1 for i in range(10)] for i in range(5)];
for i in range(5):
    print(a[i])
print("\n")
b=[[a[i][j] for i in range(5)] for j in range(10)];
for i in range(10):
    print(b[i])