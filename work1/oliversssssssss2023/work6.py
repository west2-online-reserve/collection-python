def numbers_occurrence(numbers):
    numbers_dict = {}
    for number in numbers:
        if number in numbers_dict:
            numbers_dict[number] += 1
        else:
            numbers_dict[number] = 1
    return numbers_dict

