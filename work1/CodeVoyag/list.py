old_list = ["a", "b", "c", 1, 2, 3,]
out = []
for i in old_list:
    if type(i) == int:
        out.append(i)

print(sorted(out))