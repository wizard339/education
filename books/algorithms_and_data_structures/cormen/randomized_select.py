from random import randint


def randomized_partition(arr, p, r):
    i = randint(p, r)
    arr[p], arr[i] = arr[i], arr[p]
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def randomized_select(arr, p, r, i):
    
    if p == r:
        return arr[p]
    q = randomized_partition(arr, p, r)
    k = q - p + 1
    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q, i)
    else:
        return randomized_select(arr, q + 1, r, i - k)


if __name__ =='__main__':
    b = [5, 3, 4, 6, 1, 2, 0]
    print(f"Initial array: {b}")
    for i in range(1, len(b)+1):
        print(randomized_select(b, 0, len(b) - 1, i))
