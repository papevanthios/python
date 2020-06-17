#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    score_max = scores[0]
    sum_max = 0
    score_min = scores[0]
    sum_min = 0
    for i in range(len(scores)):
        if scores[i] > score_max:
            score_max = scores[i]
            sum_max += 1
        elif scores[i] < score_min:
            score_min = scores[i]
            sum_min += 1

    return sum_max , sum_min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
