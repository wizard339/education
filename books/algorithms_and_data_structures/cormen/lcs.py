"""longest common subsequence"""


def lcs_length(x: list, y: list) -> int:
    m = len(x)
    n = len(y)
    # array for storing values of the lengths of the subsequences
    c = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, m):

        for j in range(1, n):

            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1

            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                
            else:
                c[i][j] = c[i][j - 1]
    return c


if __name__=='__main__':
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']
    print(lcs_length(X, Y))
    
