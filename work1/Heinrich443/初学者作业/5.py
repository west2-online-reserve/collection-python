d = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"}
res = {}
for k in d.keys():
    if k % 2 == 1:
        res[k] = d[k]
print(res)