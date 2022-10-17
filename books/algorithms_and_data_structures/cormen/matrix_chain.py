import sys


def matrix_chain_order(p: list) -> tuple:
    """function for finding the most efficient way of multiplication"""
    n = len(p)
    # the array with a minimum number of multiplications (it's equal to zero when multiplying a single matrix)
    m = [[0 for x in range(n + 1)] for y in range((n + 1))]
    # the array where indexes of the split positions (insertions of parenthesis) are stored
    s = [[None for x in range(n + 1)] for y in range((n + 1))]

    # the lenth of the subsequence
    for lnt in range(2, n + 1):
        
        for i in range(1, n - lnt + 2):
            
            j = i + lnt - 1
            m[i][j] = sys.maxsize
            
            k = 1
            while j < n and k <= j - 1:
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
                    
                k += 1

    return (m, s)

def matrix_chain_multiply(p: list) -> int:
    """returns the optimal number of scalar multiplications"""
    n = len(p)
    return matrix_chain_order(p)[0][1][n - 1]


def print_optimal_parens(s: list, i: int, j: int) -> str:
    """prints the optimal placement of parenthesis"""
    if i == j:
        print(f" A_{i}", end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(')', end=' ')


if __name__ == "__main__":
    a = [30, 35, 15, 5, 10, 20, 25]
    print(f'The minimum cost of multiplying a chain of matrices is {matrix_chain_multiply(a)}.')
    b = matrix_chain_order(a)[1]
    print('The optimal placement of parenthesis:')
    print_optimal_parens(b, 1, 5)
