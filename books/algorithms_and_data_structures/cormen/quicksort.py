from random import randint

def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q)
        quicksort(arr, q + 1, r)


def partition(arr, p, r):
    x = arr[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while arr[j] < x:
            j -= 1
        i += 1
        while arr[i] > x:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j


def randomized_partition(arr, p, r):
    i = randint(p, r)
    arr[p], arr[i] = arr[i], arr[p]
    return partition(arr, p, r)


def randomized_quicksort(arr, p, r):
    if p < r:
        q = randomized_partition(arr, p, r)
        randomized_quicksort(arr, p, q)
        randomized_quicksort(arr, q + 1, r)


if __name__ == '__main__':
    a = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    print(f"Before: {a}")
    quicksort(a, 0, len(a) - 1)
    print(f"After: {a}")
    b = a = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    print(f"Before: {b}")
    randomized_quicksort(b, 0, len(b) - 1)
    print(f"After: {b}")
    
