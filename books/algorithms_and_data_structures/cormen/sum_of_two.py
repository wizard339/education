from merge_sort import merge_sort


def sum_of_two(arr, x):
    """
    Input::  `arr` is the array of the real numbers.
    Output:: `x` is the number for which need to get an answer to the question: is it possible
             to represent this number as the sum of two numbers from the array `arr`.
    """
    # sorting the array
    merge_sort(arr, 0, len(arr) - 1)

    # create the two pointer from both ends of the array
    i, j = 0, len(arr) - 1
    # repeat the loop until both pointers meet
    while i != j:
        s = arr[i] + arr[j]
        if s == x:
            return f'Yes, the number {x} can be represented as the sum of two numbers {arr[i]} \
                     and {arr[j]} from an array {arr}.'
        elif s > x:
            j -= 1
        else:
            i += 1
    return f'No, the number {x} can not be represented as the sum of two numbers from an array {arr}.'


if __name__ == '__main__':
    a = [3, 41, 52, 26, 38, 57, 9, 49]
    print(sum_of_two(a, 98))
    
