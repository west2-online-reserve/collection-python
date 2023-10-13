def count_numbers(list):
    counts = {}
    for num in list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

numbers = [1,2,3,2,3,3,4,5,5,6]
result = count_numbers(numbers)
print(result)
