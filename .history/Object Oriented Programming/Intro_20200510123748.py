from os import system, name 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
clear() 

class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
        
    def bark(self):
        print('Woof! My name is {}' .format(self.name))

my_dog = Dog(breed = 'Lab', name = 'Sammy', spots  = False)
# print(my_dog.breed)
# print(my_dog.name) 
# print(my_dog.spots)
# my_dog.bark()
