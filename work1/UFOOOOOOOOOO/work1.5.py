name = {102301600: "小明",  102301601: "小红", 102301602: "李华", 102301603: "夏洛"}
delete = []
for num in name:
    if num % 2 == 0:
        delete.append(num)
for num in delete:
    name.popitem()

    # print(name.popitem())
for num in name:
    print(f"{num}:name[num]")