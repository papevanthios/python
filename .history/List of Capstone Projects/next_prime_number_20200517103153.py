'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

import HeaderOfFiles

my_list = []
number = 1
while True:
    x = input("Give me next prime number or type 's' to stop programm: ")
    if x == 's':
        break
    else: 
        i = 2
        number += 1
        while i > 0:
            new_num = number
            
            if new_num % i == 0:
                if i not in my_list:
                    my_list.append(i)
                    print("Next Prime Number is: {}".format(i))
                    break
                else:
                    number += 1
                # new_num = new_num/i
                i = 2
            else:
                i += 1
        
