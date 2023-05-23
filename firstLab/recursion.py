#recursive method

def fibonacciRecursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)

