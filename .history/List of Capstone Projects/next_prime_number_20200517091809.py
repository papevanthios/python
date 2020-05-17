'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

import HeaderOfFiles

def next_prime(number):
    '''
    Generate the next prime number
    '''



i = 1
number = 1
while True:
    number += 1
    int = 2
    my_list = []
    x = input("Give me next prime number or type 'stop' to stop programm: ")
    if x == 'stop':
        break
    else:
        while i > 0:
            if number % i == 0:
                if i not in my_list:
                    my_list.append(i)
                    print(i)
                number = number/i
                i += 1
                print(number)
            if number == 1:
                break

        continue

