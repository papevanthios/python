'''
https://www.hackerrank.com/challenges/mini-max-sum/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum_min = arr[0]
    sum_max = 0
    for i in range(1, len(arr) - 1):
        sum_min += arr[i]
        sum_max += arr[i]
    print(sum_min , sum_max + arr[-1])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
