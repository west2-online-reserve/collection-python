def count_number(numbers):
    number_count = {}
    for num in numbers:
        if num in number_count:
            number_count[num] += 1
        else:
            number_count[num] = 1
    return number_count
my_list = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
result = count_number(my_list)
print(result)


