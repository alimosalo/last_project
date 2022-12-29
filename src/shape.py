import unittest
import operator
from math import sqrt
class Point:
    def __init__(self,x:float,y:float)->None:
        self.x = x
        self.y = y
    def print_funtion(self):
        print(f"x: {self.x}, y: {self.y}")
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)       
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)       

class Shape:
    def __init__(self) -> None:
        self.vertices=[]
    def add_vertex(self,p:Point):
        self.vertices.append(p)
    def print_function(self):
        print(f"number of vertices: {len(self.vertices)}")
    def perimeter(self):
        side = []
        position =self.vertices[0]
        for i in self.vertices:
            side_vec=position-i
            side_length=sqrt(side_vec.x**2+side_vec.y**2)
            side.append(side_length)
            position=i
        return sum(side)

a = Shape()
a.add_vertex(Point(2,2))
a.add_vertex(Point(3,2))
a.add_vertex(Point(2,2))
print(a.perimeter())

