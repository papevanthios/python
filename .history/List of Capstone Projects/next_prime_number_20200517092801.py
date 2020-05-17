'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

import HeaderOfFiles

def next_prime(number):
    '''
    Generate the next prime number
    '''




number = 1
while True:
    number += 1
    print("Number cal: {}".format(number))
    new_num = number
    i = 2
    my_list = []
    x = input("Give me next prime number or type 'stop' to stop programm: ")
    if x == 's':
        break
    else:
        while i > 0:
            if new_num % i == 0:
                if i not in my_list:
                    my_list.append(i)
                    print("Next Prime Number is: {}".format(i))
                new_num = new_num/i
            i += 1
            print("i = {}".format(i))
            #print(new_num)
            if new_num == 1:
                break

        continue

