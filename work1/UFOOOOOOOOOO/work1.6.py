def count(numList):
    result = {}
    for num in numList:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result


# numList1 = [1, 23, 123, 1, 3, 1, 3]
# print(count(numList1))
