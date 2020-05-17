'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

import HeaderOfFiles

def next_prime(number):
    '''
    Generate the next prime number
    '''



my_list = []
number = 1
while True:
    x = input("Give me next prime number or type 'stop' to stop programm: ")
    if x == 's':
        break
    else:
        number += 1
        print("Number cal: {}".format(number))
        new_num = number
        i = 2
    
        while i > 0:
            if new_num % i == 0:
                if i not in my_list:
                    my_list.append(i)
                    print("Next Prime Number is: {}".format(i))
                    break
                new_num = new_num/i
                if new_num == 1:
                    new_num = number + 1
                i == 2
            else:
                i += 1
            print("i = {}".format(i))


            # print(new_num)
            # print(my_list)

        continue

