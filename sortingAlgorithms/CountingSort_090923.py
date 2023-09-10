def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = [-1] * len(arr)
    
    for num in arr:
        count[num] += 1
    
    idx = 0
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr[idx] = i
            idx += 1
            count[i] -= 1
    return sorted_arr

# User input and demo
# arr = list(map(int, input("Enter space-separated numbers: ").split()))
# sorted_arr = counting_sort(arr)
# print("Sorted Array:", sorted_arr)
