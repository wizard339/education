def counting_sort_for_radix(arr, place_value):
    # we can assume hat the number of digits used to represent all numbers on the
    # place_value position is not greater than 10
    counts_arr = [0] * 10
    input_size = len(arr)
    result_arr = [0] * input_size

    # place_el is the value of the current place value of the current element, e.g. if
    # the current element is 123, and the place_value is 10, the place_el is equal to 2 
    for i in range(input_size):
        place_el = (arr[i] // place_value) % 10
        counts_arr[place_el] += 1

    for i in range(1, 10):
        counts_arr[i] += counts_arr[i - 1]

    for i in range(input_size - 1, -1, -1):
        place_el = (arr[i] // place_value) % 10
        counts_arr[place_el] -= 1
        result_arr[counts_arr[place_el]] = arr[i]

    return result_arr


def radix_sort(arr):
    k = max(arr)

    # find the number of digits in the maximum element
    d = 1
    while k >= 10:
        k /= 10
        d += 1

    place_value = 1

    # we pass from the smaller digit of the number to the larger one
    result_arr = arr
    while d > 0:
        result_arr = counting_sort_for_radix(result_arr, place_value)
        place_value *= 10
        d -= 1

    return result_arr


if __name__ == '__main__':
    a = [4, 817, 3, 100, 50, 5]
    print(radix_sort(a))
