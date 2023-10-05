#创建一个函数，这个函数可以统计一个只有数字的列表中所有数字的个数，通过字典方式返回
#自设输入样例：1 1 2 3 2 9 5
#自设输出样例：{1: 2, 2: 2, 3: 1, 9: 1, 5: 1}

def calculate( num_list ):
    dict = { }
    for x in num_list:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1

    return dict

# main函数
input_str = input("请有间隔地输入纯数字列表：")
list = input_str.split()
num_list = [eval(num) for num in list]

dict0 = calculate(num_list)

print(dict0)