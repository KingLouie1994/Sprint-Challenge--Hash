def intersection(arrays):

    """
    YOUR CODE HERE
    """

    result = []
    ht = {}

    for array in arrays:
        for item in array:
            if item in ht:
                ht[item] += 1
            else:
                ht[item] = 1

    for index, number in enumerate(ht):
        if ht[number] == len(arrays):
            result.append(number)

    return result

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
