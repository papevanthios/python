'''
Fibonacci Sequence
'''

import HeaderOfFiles

def fibonacciSeq(number):
    '''
    Generate Fibonacci Sequence to the given number.
    '''

    a = 1
    b = 1
    for i in range(number):
        print(a)
        print(b)
        a,b = b, a+b
        
    

while True:
    try:
        f = int(input("Enter a number for Fibonacci: "))
        break
    except:
        print("Give me a number please!")

fibonacciSeq(f)