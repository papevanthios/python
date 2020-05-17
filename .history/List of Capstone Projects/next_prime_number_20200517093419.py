'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

import HeaderOfFiles

def next_prime(number):
    '''
    Generate the next prime number
    '''




number = 1
end = 2
while True:
    x = input("Give me next prime number or type 'stop' to stop programm: ")

    # number += 1
    # print("Number cal: {}".format(number))
    # new_num = number
    # i = 2
    # my_list = []
    if x == 's':
        break
    else:
        end += 1
        for val in range(2, end + 1): 
            if val > 1: 
                for n in range(2, val//2 + 2): 
                    if (val % n) == 0: 
                        break
                    else: 
                        if n == val//2 + 1: 
                            print(val) 



        # while i > 0:
        #     if new_num % i == 0:
        #         if i not in my_list:
        #             my_list.append(i)
        #             print("Next Prime Number is: {}".format(i))
        #         new_num = new_num/i
        #     i += 1
        #     print("i = {}".format(i))
        #     #print(new_num)
        #     if new_num == 1:
        #         break

        continue

