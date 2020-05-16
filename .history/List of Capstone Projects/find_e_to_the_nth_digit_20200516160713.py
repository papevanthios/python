'''
Find E to the Nth Digit - Just like the previous problem, but with e instead of π (pi). Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
'''

import HeaderOfFiles
import math

def e_func(number):
    '''
    Generate E to the given number.
    '''
    return round(math.e, number)

while True:
    try:
        e = int(input("Enter a number between 0 to 15 for E programm: "))
        if  e > 15:
            print("Give a number between 0 and 15 please!")
            continue
        break
    except ValueError:
        print("Give me a number please!")

print(e_func(e))
