'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

import HeaderOfFiles

def prime_factor(number):
    '''
    Finding and display all Prime Factors
    '''
    my_list = []
    i = 1
    while i < number:
        if number % i == 0:
            my_list.append(i)
            number = number/i
            print(number)
            i = 2
        i += 1




    # for i in range(2, number):
    #     if number%i == 0:
    #         print(i)
    #         my_list.append(i)
    #         number = number/i
    #         print(number)
    #         i = 2
            

    print(my_list)


# while True:
#     try:
#         x = int(input("Give me a number to find all Prime Factors: "))
#         break
#     except ValueError:
#         print("Give a number please!")

prime_factor(120)