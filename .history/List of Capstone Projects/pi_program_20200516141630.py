'''
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
'''

import HeaderOfFiles


while True:
    try:
        f = int(input("Enter a number between 0 to 100 for Pi programm : "))
        if  f > 100:
            print("Give a number between 0 and 100 please!")
            continue
        break
    except ValueError:
        print("Give me a number please!")
