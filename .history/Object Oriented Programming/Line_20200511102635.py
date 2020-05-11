import math 
from ../HeaderFiles import Header1
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        print(((x2-x1)**2 + (y2-y1)**2)**0.5)


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
