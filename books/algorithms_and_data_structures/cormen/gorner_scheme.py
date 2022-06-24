def gorner_scheme(arr, x):
    """
    Input::  `arr` is an array with coefficients of the polynomial.
    Output:: `x` the point for which need to find the value of the polynomial.
    """
    res = arr[-1]
    
    for i in range(len(arr) - 1, 0, -1):
        res = res * x + arr[i-1]

    res += arr[0]
    return res

if __name__ == '__main__':
    gorner_scheme([0, 1, 2, 3, 4], 2)
    
