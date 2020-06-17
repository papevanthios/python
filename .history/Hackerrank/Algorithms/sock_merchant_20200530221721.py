'''
https://www.hackerrank.com/challenges/sock-merchant/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    sum = 0
    sum_1 = 0
    sum_2 = 0
    for i in range( n - 1 ):
        if ar[i] == ar[i+1]:
            sum += 1
            ar[i] = ''
            ar[i + 1] = ''
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
