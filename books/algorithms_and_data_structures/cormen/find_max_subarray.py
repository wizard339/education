def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(arr, low, high):
    """
    the version of the algorithm based on the 'devide and conquere' method is executed 
    in O(n*lg(n)) time
    """
    if high == low:
        return (low, high, arr[low])

    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_max_subarray(arr, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(arr, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def find_max_subarray_fast(arr):
    """
    the version of the algorithm based on the dynamic programming method is executed in
    linear time O(n)
    """
    cur_sum = arr[0]
    max_sum = arr[0]
    # bounds of the maximum subarray
    low, high = 0, 0

    for i in range(1, len(arr)):
        if cur_sum > 0:
            cur_sum += arr[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
                high = i
        else:
            cur_sum = arr[i]
            low = i
    return (low, high, max_sum)
    


if __name__ == '__main__':
    a = [1, 5, -5, 17, -14, 5, -1]
    print(find_max_subarray(a, 0, len(a) - 1))
    print(find_max_subarray_fast(a))
    
