from insertion_sort import insertion_sort


def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for i in range(n)]

    # sorting elements of the arr by the buckets
    for i in range(n):
        bucket_number = int(n * arr[i])
        buckets[bucket_number].append(arr[i])

    # sorting each bucket using insertion_sort
    for i in range(n):
        insertion_sort(buckets[i])

    # combining into one resulting array
    result_arr = []
    for i in range(n):
        result_arr += buckets[i]

    return result_arr
    

if __name__=='__main__':
    a = [0.15, 0.29, 0.65, 0.44, 0.21, 0.91, 0.40]
    print(bucket_sort(a))
    
