def counting_sort(A, B, k):
    C = [0] * k
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    # now C[i] contains the number of elements equal to i
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    # now C[i] contains the number of elements not exceeding i
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1


if __name__ == '__main__':
    a = [4, 8, 3, 1, 5, 5]
    b = [0] * len(a)
    counting_sort(a, b, 10)
    print(b)
    
