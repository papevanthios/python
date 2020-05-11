from os import system, name 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
clear() 
import math

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        print(math.pi*self.radius**2*self.height)
    
    def surface_area(self):
        print(math.pi*self.radius**2)

c= Cylinder()
c.volume
