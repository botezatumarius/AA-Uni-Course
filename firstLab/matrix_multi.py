#matrix multiplication method

def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def fib_matrix_mult(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        F = [[1, 1], [1, 0]]
        for i in range(2, n):
            F = matrix_mult(F, [[1, 1], [1, 0]])
        return F[0][0]