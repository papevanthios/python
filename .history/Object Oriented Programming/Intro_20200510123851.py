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

class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle(2)

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())