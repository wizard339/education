def len_rec(arr):
    """
    recurrent version of len function in array
    """
    if not arr:
        return 0
    return 1 + len_rec(arr[1:])

print(len_rec([1, 2, 3]))
