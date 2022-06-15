def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


def main():
    a = [3, 8, 2, 4, 10, 11, 1]
    print('Unsorted: ', a)
    b = selection_sort(a)
    print('Sorted: ', b)


if __name__ == '__main__':
    main()
