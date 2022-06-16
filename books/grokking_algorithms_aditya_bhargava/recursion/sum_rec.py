import numbers


def sum_rec(arr: list) -> numbers.Number:
    """
    recurrent version of sum function of array
    """
    # base case
    if not arr:
        return 0
    # recursive case
    return arr[0] + sum_rec(arr[1:])


print(sum_rec([1, 2, 3, 6]))
