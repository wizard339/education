inv_counter_ = 0


def num_inversions(arr, p, r):
    if p < r:
        q = (p + r) // 2
        num_inversions(arr, p, q)
        num_inversions(arr, q + 1, r)
        merge(arr, p, q, r)
    else:
        return
    return f'Number of inversions: {inv_counter_}'


def merge(arr, p, q, r):
    global inv_counter_
    # create a copy of array
    left = arr[p:q + 1]
    right = arr[q + 1:r + 1]
    n1 = len(left)
    n2 = len(right)
    # create pointers for indexing in the `left`, `right` and `arr` arrays
    i = 0
    j = 0
    while i < n1:
        while j < n2:
            if left[i] > right[j]:
                inv_counter_ += 1
            j += 1
        j = 0
        i += 1


if __name__ == '__main__':
    a = [2, 4, 1, 3, 5]
    print(a)
    print(num_inversions(a, 0, len(a) - 1))
