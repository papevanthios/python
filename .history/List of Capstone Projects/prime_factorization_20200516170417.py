'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

import HeaderOfFiles
from collections import OrderedDict

def prime_factor(number):
    '''
    Finding and display all Prime Factors
    '''
    my_list = []
    i = 2
    while i < number + 1:
        if number % i == 0:

            my_list.append(i)
            number = number/i
            print(number)
            i = 2
        else:
            i += 1

    print(OrderedDict(my_list))

# while True:
#     try:
#         x = int(input("Give me a number to find all Prime Factors: "))
#         break
#     except ValueError:
#         print("Give a number please!")

prime_factor(120)