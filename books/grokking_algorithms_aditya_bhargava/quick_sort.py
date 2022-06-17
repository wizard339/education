import random
import doctest


def quick_sort(arr):
    """
    Tests for doctest:
        >>> print(quick_sort([1, 2, 3, 4, 5]))
        [1, 2, 3, 4, 5]
        >>> print(quick_sort([1]))
        [1]
        >>> print(quick_sort([5, 4, 3, 2, 1]))
        [1, 2, 3, 4, 5]
        >>> print(quick_sort([3, 7, 1, 0, 9]))
        [0, 1, 3, 7, 9]
    """
    # base case, when the array is sorted
    if len(arr) < 2:
        return arr
    else:
        # choose the random element as pivot element
        pivot = random.choice(arr)

        # a subarray with values less or equal pivot
        less = []
        # a subarray with values greater pivot
        greater = []
        # a subarray with values equal pivot
        equal = []
        for elem in arr:
            if elem < pivot:
                less.append(elem)
            elif elem > pivot:
                greater.append(elem)
            else:
                equal.append(elem)

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
