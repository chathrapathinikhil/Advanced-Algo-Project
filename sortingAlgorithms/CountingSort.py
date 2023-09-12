
import time

start = time.process_time()


def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [-1] * len(arr)
    for i in arr:
        count[i] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr

# arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Sorted Array:", counting_sort(arr))

end = time.process_time()
print(end - start)