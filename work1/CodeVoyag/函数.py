numbers = [1, 2, 3, 4, 2, 1, 3, 4, 5, 5]


def count_numbers(numbers):
    count_dict = {}  

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    return count_dict


result = count_numbers(numbers)
print(result)

