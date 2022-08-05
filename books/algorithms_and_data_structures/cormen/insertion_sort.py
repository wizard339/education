def insertion_sort(arr, ascending=True, inplace=True):
    """
    Аlgorithm `Insertion sort` is convenient for sorting short sequences. 

    Алгоритм `сортировки вставками` удобен для сортировки коротких последовательностей.
    
    This is the way cards are usually sorted: holding the already ordered cards in the left hand and
    taking the next card with the right hand, we insert it into the right place, comparing it with the
    existing ones and going straight to the left.

    Именно таким способом обычно сортируют карты: держа в левой руке уже упорядоченные карты и взяв
    правой рукой очереднуб карту, мы вставляем ее в нужное место, сравнивая с имеющимися и идя справо
    налево.
    __________________
    Input::  `arr` is the sequence of n numbers (a1, a2, ..., an);
             `ascending` is the mode of sorting (True - by ascending from min to max,
                                                 False - by descending from max to min);
             `inplace` is the sorting in place.
    Output:: `arr` is the permutation (a1', a2', ..., an') of the initial sequence for which
    a1'<= a2'<= ... <= an'.
    __________________
    
    Example input::  [31, 41, 59, 26, 41, 58].
    Example output:: [26, 31, 41, 41, 58, 59].
    """

    # if `inplace=False` then we create a copy of list
    res_arr = list(arr) if not inplace else arr
    if len(res_arr) == 1:
        return res_arr
    
    for j in range(1, len(res_arr)):
        key = res_arr[j]
        # add `arr[j]` to the sorted part `arr[1...j - 1]`
        i = j - 1
        # if sorting by ascending then we move the element to the left until it is greater than the
        # previous element;
        # if sorting by descending then we move the element to the left until it is less than the
        # previous element
        while i >= 0 and ((res_arr[i] > key) if ascending else
                          (res_arr[i] < key)):
            res_arr[i + 1] = res_arr[i]
            i = i - 1
        res_arr[i + 1] = key
    return res_arr


def insertion_binary_sort(arr, inplace=True):
    res_arr = list(arr) if not inplace else arr
    for j in range(1, len(res_arr)):
        i = j - 1
        key = res_arr[j]
        loc = bin_search(res_arr[:j], key)

        # Move all elements after location to create space
        while i >= loc:
            res_arr[i + 1] = res_arr[i]
            i -= 1
        res_arr[i + 1] = key

    return res_arr


def bin_search(arr, x):
    """
    It is the specisal realization of the binary search for using in the insertion sorting.
    The peculiarity of the implementation is that if the search fails, the function returns the left bound.
    """
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

    return l


if __name__ == '__main__':
    initial_seq = [31, 41, 59, 26, 41, 58]
    print('Initial sequence: ', initial_seq)

    result_seq_asc = insertion_sort(initial_seq)
    print(f'Sorted sequence by ascending: {result_seq_asc}')

    result_seq_desc = insertion_sort(initial_seq, ascending=False)
    print(f'Sorted sequence by descending: {result_seq_desc}')

    result_seq_ins_bin = insertion_binary_sort(initial_seq)
    print(f'Sorted sequence by insertion-binary-sort: {result_seq_ins_bin}')
