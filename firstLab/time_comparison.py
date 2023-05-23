#the code that I used to create the time comparison tables

from recursion import *
from iteration import *
from binet import *
from dynamic import *
from golden_ratio import *
from matrix_expo import *
from matrix_multi import *
import time
import os
import sys

sys.setrecursionlimit(20000)

os.system('clear')

firstSet = [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45]
secondSet = [500, 1000, 1300, 1900, 2400, 3500, 5500, 6969, 10000, 12245, 14780, 16000, 21000,25000,30000,35000,40000]

algorithmTime = []

"""

#TESTING THE FIRST SET OF INPUTS

for i in firstSet:
    start_time = time.time()
    fibonacciRecursion(i)
    algorithmTime.append(time.time() - start_time)

print('  ',end='')

for i in range(0,len(firstSet)):
    if (i == len(firstSet)-1):
        print(f"{firstSet[i] : ^6}")
    else:
        print(f"{firstSet[i] : ^6}",' ',end = '')

#recursive method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{1 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in firstSet:
    start_time = time.time()
    fibonacciIteration(i)
    algorithmTime.append(time.time() - start_time)

#iteration method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{2 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in firstSet:
    start_time = time.time()
    fibonacciDynamic(i)
    algorithmTime.append(time.time() - start_time)

#dynamic method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{3 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in firstSet:
    start_time = time.time()
    fibonacciBinet(i)
    algorithmTime.append(time.time() - start_time)

#binet method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{4 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in firstSet:
    start_time = time.time()
    fibonacciMatrix(i)
    algorithmTime.append(time.time() - start_time)

#matrix method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{5 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')


algorithmTime.clear()

for i in firstSet:
    start_time = time.time()
    fibonacciGolden(i)
    algorithmTime.append(time.time() - start_time)

#golden ratio method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{6 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

"""

#TESTING THE SECOND SET OF INPUTS

for i in secondSet:
    start_time = time.time()
    fibonacciIteration(i)
    algorithmTime.append(time.time() - start_time)

print('  ',end='')

for i in range(0,len(secondSet)):
    if (i == len(secondSet)-1):
        print(f"{secondSet[i] : ^7}")
    else:
        print(f"{secondSet[i] : ^6}",' ',end = '')

#iteration method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{2 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in secondSet:
    start_time = time.time()
    fibonacciDynamic(i)
    algorithmTime.append(time.time() - start_time)

#dynamic method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{3 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in secondSet:
    start_time = time.time()
    fibonacciBinet(i)
    algorithmTime.append(time.time() - start_time)

#binet method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{4 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in secondSet:
    start_time = time.time()
    fibonacciMatrix(i)
    algorithmTime.append(time.time() - start_time)

#matrix exponentiation method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{5 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in secondSet:
    start_time = time.time()
    fibonacciGolden(i)
    algorithmTime.append(time.time() - start_time)

#golden ratio method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{6 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')

algorithmTime.clear()

for i in secondSet:
    start_time = time.time()
    fib_matrix_mult(i)
    algorithmTime.append(time.time() - start_time)

#matrix multiplication method
for i in range(-1,len(algorithmTime)):
    if (i == -1):
        print(f"{7 : <1}",' ',end = '')
    else:
        if (i == len(algorithmTime)-1):
            print(f"{'%.3f' % algorithmTime[i] : ^6}")
        else:
            print(f"{'%.3f' % algorithmTime[i] : ^6}",' ',end = '')







