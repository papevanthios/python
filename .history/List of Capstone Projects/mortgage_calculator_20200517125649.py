'''
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over 
given Nth terms at a given interest rate. Also figure out how long it will take the 
user to pay back the loan. For added complexity, add an option for users to select 
the compounding interval (Monthly, Weekly, Daily, Continually).
'''

import HeaderOfFiles

# M for monthly payments
# P for principal
# r for interest
# n for number of payments

P = 10000
r = 1
n = 180

def mortgage_calc(P, r, n):
    return P((r(1+r)**n)/(1+r)**n-1)

# M = mortgage_calc(P, r, n)
print(int(P((r(1+r)**n)/(1+r)**n-1)))
