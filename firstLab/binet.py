#binet method

from decimal import *

def fibonacciBinet(n):
    contx = Context(prec=60,rounding=ROUND_HALF_EVEN)
    phi = Decimal((1+Decimal(5**(1/2))))
    phi1 = Decimal((1+Decimal(5**(1/2))))

    return int((contx.power(phi, Decimal(n)) - contx.power(phi1, Decimal(n))))/(2**n*Decimal(5**(1/2)))


