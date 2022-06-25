def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
    else:
        return


def merge(arr, p, q, r):
    # create a copy of array
    left = arr[p: q + 1]
    right = arr[q + 1: r + 1]

    n1 = len(left)
    n2 = len(right)
    # create pointers for indexing in the `left`, `right` and `arr` arrays
    i = 0
    j = 0
    k = p

    # until we get to the end of the array, we select the largest value
    # and put it in the desired position
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # if there are elements left in arrays
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    array_for_sort = [3, 19, 5, 5, 30, 15, 11]
    merge_sort(array_for_sort, 0, len(array_for_sort) - 1)
    print(array_for_sort)
