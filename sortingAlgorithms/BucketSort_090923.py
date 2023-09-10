def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while j >= 0 and var < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = var
    return bucket

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for i in range(bucket_count):
        # Convert index to an integer
        idx = int((arr[i] - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[idx].append(arr[i])
    
    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])

    return [val for sublist in buckets for val in sublist]

# User input and demo
# arr = list(map(float, input("Enter space-separated numbers: ").split()))
# sorted_arr = bucket_sort(arr)
# print("Sorted Array:", sorted_arr)
