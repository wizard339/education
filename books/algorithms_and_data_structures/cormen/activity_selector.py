from typing import Union


def rec_activity_selector(s: Union['list', 'tuple'], f: Union['list', 'tuple'], k: int, n: int, res=[]) -> list:
    """
    The purpose of the procedure is to collect a set of mutually compatible processes forming a set of a maximum size.

    Running time - O(n).

    Input::  
    s, f - arrays with initial and final time of processes, which are sorted by the final time in ascending order;
    the first elements of arrays (with zero index) are a fictitious process with zero start and end times
    k - subtask index;
    n - number of processes;
    res - an array for storing the mutually compatible processes.

    Output::
    A list with the mutually compatible processes forming a set of a maximum size.
    """
    m = k + 1

    while (m <= n) and (s[m] < f[k]):
        m += 1

    if m <= n:
        res.append((s[m], f[m]))
        return rec_activity_selector(s, f, m, n, res)
        
    else:
        return res


def greedy_activity_selector(s: Union['list', 'tuple'], f: Union['list', 'tuple']) -> list:
    """
    The purpose of the procedure is to collect a set of mutually compatible processes forming a set of a maximum size.

    Running time - O(n).
    
    Input::
    s, f - arrays with initial and final time of processes, which are sorted by the final time in ascending order;
    the first elements of arrays (with zero index) are a fictitious process with zero start and end times.

    Output::
    A list with the mutually compatible processes forming a set of a maximum size.    
    """
    n = len(s)
    res = [(s[1], f[1])]
    k = 1

    for m in range(2, n):

        if s[m] >= f[k]:
            res.append((s[m], f[m]))
            k = m

    return res


if __name__ == '__main__':
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(rec_activity_selector(s, f, 0, len(s) - 1))
    print(greedy_activity_selector(s, f))
    
