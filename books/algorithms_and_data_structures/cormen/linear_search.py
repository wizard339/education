def linear_search(arr, v):
    """
    Аlgorithm `Linear search` sequentially scans the array in search of an element.

    Алгоритм `линейного поиска` последовательно просматривает массив в поисках элемента.
    
    __________________
    Input::  `arr` is the sequence of n numbers (a1, a2, ..., an);
             `v` is the number we a looking for.
    Output:: `i` is the index for which v = arr[i] or a special value `NIL` if `v` not in `arr`.
    __________________
    
    Example input::  [31, 41, 59, 26, 41, 58], 20.
    Example output:: NIL.
    """
    for i in range(len(arr)):
        if arr[i] == v:
            return i
            
    return 'NIL'


if __name__ == '__main__':
    res = linear_search([31, 41, 59, 26, 41, 58], 9)
    print(f'Result: {res}.')
