

import time

start = time.process_time()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Sorted Array:", bubble_sort(arr))

# end = time.process_time()
# print(end - start)