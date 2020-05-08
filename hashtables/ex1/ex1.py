def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    ht = {}

    for index, weight in enumerate(weights):
        diff = limit-weight
        if diff in ht:
            result = [ht[diff], index]
            result.sort(reverse=True)
            return (result)
        else:
            ht[weight] = index

    return None