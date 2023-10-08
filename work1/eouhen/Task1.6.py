# Author : AnnieHathaway
def numbers(lst):
    count = {}

    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return count

# 演示一下
num = [7, 2, 2, 3, 4, 4, 4, 5, 3, 7, 7, 7, 4]
result = numbers(num)
print(result)
