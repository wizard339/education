def parent(i):
    return i // 2


def left(i):
    return 2*i


def right(i):
    return 2*i + 1


def heap_size(arr):
    return len(arr)


def heapify(arr, i):
    l = left(i)
    r = right(i)
    if l <= heap_size(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)
    return arr


if __name__ == '__main__':
    a = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    a = heapify(a, 3)
    print(a)
    
