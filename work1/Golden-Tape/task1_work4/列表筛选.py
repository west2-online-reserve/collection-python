input_str = input("请输入一个列表，例如：[1, 2, '逸一时，误一世', 3]: ")
input_list = eval(input_str)
int_list = []
for item in input_list:
    if type(item) == int:
        int_list.append(item)
for i in range(len(int_list)):
    for j in range(0, len(int_list) - i - 1):
        if int_list[j] > int_list[j + 1]:
            int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
print(int_list)