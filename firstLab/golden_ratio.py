#golden ratio method

import math
import decimal

def fibonacciGolden(n):
    if n <= 0:
        return 0
    else:
        decimal.getcontext().prec = 100  
        golden_ratio = decimal.Decimal((1 + decimal.Decimal(5).sqrt()) / 2)
        return int((golden_ratio ** n - (1 - golden_ratio) ** n) / decimal.Decimal(math.sqrt(5)))



