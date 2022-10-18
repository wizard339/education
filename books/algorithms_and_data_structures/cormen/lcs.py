"""longest common subsequence"""


def lcs_length(x: list, y: list) -> int:
    m = len(x)
    n = len(y)
    # array for storing values of the lengths of the subsequences
    c = [[0 for i in range(m)] for j in range(n)]

    for i in range(1, m):

        for j in range(1, n):

            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1

            elif c[i - 1][j] >= c[i, j - 1]:
                c[i][j] = c[i - 1][j]
                
            else:
                c[i][j] = c[i][j - 1]
    return c
