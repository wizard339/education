def binary_search_iter(arr, x):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            r = mid - 1
        elif x > arr[mid]:
            l = mid + 1

    return 'Not found!'


def binary_search_rec(arr, x, start, end):
    if start > end:
        return 'Not found!'
        
    mid = (start + end) // 2
    
    if x == arr[mid]:
        return mid
    
    if x < arr[mid]:
        return binary_search_rec(arr, x, start, mid - 1)
    else:
        return binary_search_rec(arr, x, mid + 1, end)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search_iter(a, 9))
    print(binary_search_rec(a, 9, 0, len(a) - 1))
