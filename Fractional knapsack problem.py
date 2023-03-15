def fractional_knapsack(value, weight, capacity):
    
    items = list(zip(value, weight))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0
    for v, w in items:
        if capacity == 0:
            break
            
        amount = min(w, capacity)
        total_value += amount * (v / w)
        capacity -= amount
    return total_value
