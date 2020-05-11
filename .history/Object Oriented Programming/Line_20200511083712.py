from os import system, name 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
clear() 

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        print((coor1[1] - coor1[0])**2 +(coor2[1] - coor2[0])**2)
    
    def slope(self):
        pass

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()