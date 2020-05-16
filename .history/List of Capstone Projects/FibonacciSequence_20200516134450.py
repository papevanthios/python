'''
Fibonacci Sequence
'''

import HeaderOfFiles

def fibonacci_seq(number):
    '''
    Generate Fibonacci Sequence to the given number.
    '''

    a = 0
    b = 1
    for _ in range(number):
        yield a
        a,b = b,a+b
        
    

while True:
    try:
        f = int(input("Enter a number for Fibonacci: "))
        break
    except:
        print("Give me a number please!")

print(list(fibonacci_seq(f)))