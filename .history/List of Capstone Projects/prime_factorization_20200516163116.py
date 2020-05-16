'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

import HeaderOfFiles

def prime_factor(number):
    '''
    Finding and display all Prime Factors
    '''
    my_list = []
    for i in range(1, number):
        if number%i == 0:
            my_list.append(number)
            number = number/2
    print(my_list)


while True:
    try:
        x = int(input("Give me a number to find all Prime Factors: "))
        break
    except ValueError:
        print("Give a number please!")

prime_factor(x)