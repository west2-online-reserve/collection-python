#列表
my_list = ['马保国', 12, '戴夫', 3, '喔昶', 7, 10]
int_list = [x for x in my_list if isinstance(x, int)]
int_list_sorted = sorted(int_list)
print(int_list_sorted)
