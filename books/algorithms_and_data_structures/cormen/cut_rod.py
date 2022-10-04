"""
An example of dynamic programming for solving the problem of cutting the rod.

The essence of the problem is as follows: a company buys a long steel rods
which it cuts into pieces and sells. The company's management wants to know
how best to cut the rods into pieces.
"""


# the first approach is top-down with memoization (from 'memo')
def memoized_cut_rod(p: list, n: int) -> int:
    r = [-float("inf")] * n
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: list, n: int, r: list) -> int:
    if r[n - 1] >= 0:
        return r[n - 1]
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i, r))
    r[n - 1] = q
    return q


if __name__=='__main__':
    prices = [1, 5, 8, 9, 30]
    rod_length = 3
    print(memoized_cut_rod(prices, rod_length))
