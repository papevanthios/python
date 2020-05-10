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

# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# now call function we defined above 
clear() 