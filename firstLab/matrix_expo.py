#matrix exponentiation method

def multiply(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def power(A, n):
    if n <= 1:
        return A
    else:
        B = power(A, n//2)
        C = multiply(B, B)
        if n % 2 == 0:
            return C
        else:
            return multiply(A, C)

def fibonacciMatrix(n):
    if n <= 0:
        return 0
    else:
        A = (1, 1, 0)
        B = power((1, 1, 0), n-1)
        a, b, c = B
        return b


