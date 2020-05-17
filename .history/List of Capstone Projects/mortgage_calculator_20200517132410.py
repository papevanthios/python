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

P = 100000
r = 0.005
n = 180

def mortgage_calc(P, r, n):
    M = P*((r*((1+r)**n)) / (((1+r)**n)-1))
    return M


print(round(mortgage_calc(P, r, n), 1))
# print((1+r)**n)