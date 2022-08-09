def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def partition(arr, p, r):
    # the partitioning algorithm developed by N. Lomuto
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


if __name__ == '__main__':
    a = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    print(f"Before: {a}")
    quicksort(a, 0, len(a) - 1)
    print(f"After: {a}")
