def quick_sort(arr, low, high):
    
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# test the algorithm with an example array
arr = [12, 11, 13, 5, 6]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)
