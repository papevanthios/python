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
# c for compounding intervaql(Monthly, Weekly, Daily)

while True:
    c = str(input("Give me 'M' for Monthly view, 'W' for Weekly view or 'D' for Daily."))
    if c == 'M' or c == 'W' or c == 'D':
        break
    else:
        print("Give me an option please!")


p = 100000
r = 0.005
n = 180

def mortgage_calc(p, r, n):
    return p*((r*((1+r)**n)) / (((1+r)**n)-1))

M = round(mortgage_calc(p, r, n), 1)
print("Monthly Payments are: {}".format(M))
if c == 'M':
    print("It will take you {} months to pay back the loan.".format(round(p/M) * ))
elif c == 'W':
    print("It will take you {} weeks to pay back the loan.".format(round(p/M) * 4))
elif c == 'D':
    print("It will take you {} days to pay back the loan.".format(round(p/M) * 30))

print(M*n-100000)