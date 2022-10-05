def matrix_chain_order(p: list) -> tuple:
    n = len(p) - 1
    m = [[0] * n] * n 
    s = [[None] * (n-1)] * (n-1)
    # for i in range(0, n):
    #     m[i][i] = 0
    for lnt in range(2, n+1):
        for i in range(1, n-lnt+1):
            j = i + lnt - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
            
    return (m, s)


if __name__ == "__main__":
    a = [10, 15, 20, 25]
    b, c = matrix_chain_order(a)
    print(b)
    print(c)
    
