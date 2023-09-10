def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    n = len(arr)
    output = [0] * n
    
    while max_num // exp > 0:
        counting = [0] * 10
        for i in arr:
            counting[(i // exp) % 10] += 1
        for i in range(1, 10):
            counting[i] += counting[i-1]
        for i in range(n-1, -1, -1):
            output[counting[(arr[i] // exp) % 10] - 1] = arr[i]
            counting[(arr[i] // exp) % 10] -= 1
        for i in range(n):
            arr[i] = output[i]
        exp *= 10
    return arr

# User input and demo
# arr = list(map(int, input("Enter space-separated numbers: ").split()))

# sorted_arr = radix_sort(arr)
# print("Sorted Array:", sorted_arr)
