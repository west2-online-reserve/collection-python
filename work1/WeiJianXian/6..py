num_list = [123, 122, 133, 236, 2266, 22552, 25522, 6511, 223, 122, 1223, 1233, 123]


def fun(num_list):
    out_dict = {}
    for i in num_list:
        out_dict[i] = 0

    for i in num_list:
        out_dict[i] += 1
    return out_dict


print(fun(num_list))
