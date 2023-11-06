dict1 = {102304201: "小林", 102304202: "小岳", 102304203: "小蔡", 102304204: "小赵"}
dict2 = []
for key in dict1:
    if key % 2 == 0:
        dict2.append(key)
for key in dict2:
    dict1.pop(key)
print(dict1)