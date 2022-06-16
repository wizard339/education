def max_rec(arr):
    """
    recurrent version of searching max value function in array
    """
    if len(arr) == 1:
        return arr[0]
    return max_rec(arr[1:]) if arr[0] < max_rec(arr[1:]) else arr[0]

print(max_rec([1, 200, 3]))
