#dynamic programming method

def fibonacciDynamic(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacciDynamic(n-1, memo) + fibonacciDynamic(n-2, memo)
        return memo[n]


