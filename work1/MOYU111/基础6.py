num_list = [111, 112, 113, 111, 123, 111, 112, 112, 113, 112, 113, 1234, 123]


def fun(num_list):
    out_dict = {}
    for i in num_list:
        out_dict[i] = 0

    for i in num_list:
        out_dict[i] += 1
    return out_dict


print(fun(num_list))