'''
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
'''

import HeaderOfFiles
import math

def pi_func(number):
    '''
    Generate PI to the given number.
    '''
    return round(math.pi, number)

while True:
    try:
        p = int(input("Enter a number between 0 to 100 for Pi programm : "))
        if  p > 100:
            print("Give a number between 0 and 100 please!")
            continue
        break
    except ValueError:
        print("Give me a number please!")

print(pi_func(p))
print(math.pi)