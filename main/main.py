def knapsack(weights, values, max_weight):
    n = len(weights)

    #init the first role
    result = [0] * (max_weight + 1)

    for i in range(n):
        next_result = result[:]
        for j in range(weights[i], max_weight + 1):
            next_result[j] = max(values[i] + result[j - weights[i]], result[j])
        result = next_result
    return result[max_weight]
