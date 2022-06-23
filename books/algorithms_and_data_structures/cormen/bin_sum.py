def bin_sum(arr1, arr2):
    """
    Input::  two n-element binary numbers written as arrays `arr1` and `arr2`.
    Output:: the (n+1)-element array which is the sum of `arr1` and `arr2`.
    ----------
    Example input::  bin_sum([1, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1]).
    Example output:: [1, 1, 1, 0, 0, 0, 1].
    """
    
    mem = 0
    res = [0] * (len(arr1) + 1)
    
    for j in range(len(arr1) - 1, -1, -1):
        s = arr1[j] + arr2[j] + mem
        if s <= 1:
            res[j + 1] = s
            mem = 0
        elif s == 2:
            res[j + 1] = 0
            mem = 1
        elif s == 3:
            res[j + 1] = 1
            mem = 1

    if mem > 0:
        res[0] = 1
    
    return res


if __name__ == '__main__':
    a = [1, 1, 0, 0, 1, 0]
    b = [1, 1, 1, 1, 1, 1]
    print(bin_sum(a, b))
    
