from typing import Union


def rec_activity_selector(s: Union['list', 'tuple'], f: Union['list', 'tuple'], k: int, n: int, res=[]) -> list:
    m = k + 1

    while (m <= n) and (s[m] < f[k]):
        m += 1

    if m <= n:
        res.append((s[m], f[m]))
        return rec_activity_selector(s, f, m, n, res)
        
    else:
        return res


if __name__ == '__main__':
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(rec_activity_selector(s, f, 0, len(s) - 1))
