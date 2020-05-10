class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
        
    def bark(self):
        print('Woof!')











my_dog = Dog(breed = 'Lab', name = 'Sammy', spots  = False)
print(my_dog.breed)
print(my_dog.name) 
print(my_dog.spots)

import sys
sys.stderr.write("\x1b[2J\x1b[H")