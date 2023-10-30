input_list = input("")
input_items = input_list.split(',')
integer_list = []
for item in input_items:
    if item.isdigit():
        integer_list.append(int(item))
sorted_integer_list = sorted(integer_list)
print(sorted_integer_list)
