'''
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''

import HeaderOfFiles

def fibonacci_seq(number):
    '''
    Generate Fibonacci Sequence to the given number.
    '''

    first_number = 0
    second_number = 1
    for _ in range(number):
        yield first_number
        first_number, second_number = second_number, first_number+second_number

while True:
    try:
        f = int(input("Enter a number for Fibonacci: "))
        break
    except ValueError:
        print("Give me a number please!")

print(list(fibonacci_seq(f)))

