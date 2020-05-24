'''
We define a modified Fibonacci sequence using the following definition:

Given terms ti and ti+1 where ie(0, +inf), term ti+2 is computed using the following relation: ti+2 = ti + (ti+1)^2

For example, if t1 = 0 and t2 = 1,
t3 = 0 + 1^2=1,
t4 = 1 + 1^2=2,
t5 = 1 + 2^2=5,
and so on.
Given three integers, t1, t2, and n, compute and print the nth term of a modified Fibonacci sequence.

Function Description
Complete the fibonacciModified function in the editor below. It must return the nth number in the sequence.
fibonacciModified has the following parameter(s):
t1: an integer
t2: an integer
n: an integer
Note: The value of tn may far exceed the range of a 64-bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to compensate for the size of the result.

Input Format
A single line of three space-separated integers describing the respective values of t1, t2, and n.

Output Format
Print a single integer denoting the value of term  in the modified Fibonacci sequence where the first two terms are  and .

Sample Input
0 1 5

Sample Output
5

Explanation
The first two terms of the sequence are t1 = 0 and t2 = 1, which gives us a modified Fibonacci sequence of {1,1,2,5,27,...}. Because n = 5, we return the 5th term.
https://www.hackerrank.com/challenges/fibonacci-modified/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    t3 = t1 + t2**2
    if n <= 1:
        return t3
    else:
        return (fibonacciModified(t2, t3, n-1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])
 
    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n-2)

    fptr.write(str(result) + '\n')

    fptr.close()
