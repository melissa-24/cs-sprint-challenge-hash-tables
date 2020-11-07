def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    if len(weights) > 1:
        for i in range(0, len(weights)):
            weight = weights[i]
            if weight in cache:
                val = cache[weight]
                return[i, val]
            diff = limit - weight
            cache[diff] = i
        return []
    else:
        return None