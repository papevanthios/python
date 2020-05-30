'''
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    # 1 3 2 6 1 2
    l = 0
    pairs = 0
    for i in range(n):
        l += 1
        for j in range(l, n):
            if (ar[i] + ar[j]) % k == 0:
                pairs += 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
