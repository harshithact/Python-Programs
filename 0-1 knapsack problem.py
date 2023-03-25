def knapsack(capacity, weight, value, n):
    
    if n == 0 or capacity == 0:
        return 0

    if weight[n - 1] > capacity:
        return knapsack(capacity, weight, value, n - 1)
    else:
        return max(value[n - 1] + knapsack(capacity - weight[n - 1], weight, value, n - 1),
                   knapsack(capacity, weight, value, n - 1))

capacity = 50
weight = [10, 20, 30]
value = [60, 100, 120]
n = len(value)


print(knapsack(capacity, weight, value, n))
