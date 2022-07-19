def parent(i):
    return i // 2


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def heapify(arr, i):
    l = left(i)
    r = right(i)
    if l <= heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        tmp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = tmp
        heapify(arr, largest)


def build_heap(arr):
    global heap_size
    heap_size = len(arr) - 1
    for i in range((len(arr) // 2), -1, -1):
        heapify(arr, i)


if __name__ == '__main__':
    a = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    build_heap(a)
    print(a)
    
