import unittest
import operator
from math import sqrt 
class Point:
    def __init__(self,x:float,y:float)->None:
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return Point()
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)       
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)       

class Shape:
    def __init__(self) -> None:
        self.vertices=[]
        self.side=[]
    def add_vertex(self,p:Point):
        self.vertices.append(p)
    def __repr__(self):
        return "Shape()"
    def __str__(self):
        return f"number of vertices: {len(self.vertices)}"
    def perimeter(self):
        side = []
        position =self.vertices[0]
        for i in self.vertices:
            side_vec=position-i
            side_length=sqrt(side_vec.x**2+side_vec.y**2)
            side.append(side_length)
            position=i
            self.side = side 
        return sum(side)
class Line(Shape):
    def __init__(self,p1:Point,p2:Point) -> None:
        super().__init__()
        self.add_vertex(p1)
        self.add_vertex(p2)
        pass
    def __repr__(str):
        return "Line()"
    def __str__(self):
        string1=f"p1: (x: {self.vertices[0].x}, y: {self.vertices[0].y})\n"
        string2=f"p2: (x: {self.vertices[1].x}, y: {self.vertices[1].y})"
        return string1+string2
        pass
    def area(self)->float:
        return 0 

class Triangle(Shape):
    def __init__(self,p1,p2,p3) -> None:
        super().__init__()
        self.add_vertex(p1)
        self.add_vertex(p2)
        self.add_vertex(p3)
    def __repr__(self) -> str:
        return "Triangle()"

    def __str__(self):
        string1= f"p1: (x: {self.vertices[0].x}, y: {self.vertices[0].y})\n"
        string2=f"p2: (x: {self.vertices[1].x}, y: {self.vertices[1].y})\n"
        string3=f"p3: (x: {self.vertices[2].x}, y: {self.vertices[2].y})"
        return string1+string2+string3
    def area(self)->float:
        a =self.vertices[0]
        b =self.vertices[1]
        c =self.vertices[2]
        s = 0.5*(a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y))
        return s
class Rectangle(Shape):
    def __init__(self,p1,p2) -> None:
        super().__init__()
        self.add_vertex(p1)
        self.add_vertex(p2)
        p3 = Point(p2.x,p1.y)
        p4 = Point(p1.x,p2.y)
        self.add_vertex(p3)
        self.add_vertex(p4)
    def __repr__(self):
        return "Rectangle()"
    def __str__(self):
        string1= f"p1: (x: {self.vertices[0].x}, y: {self.vertices[0].y})\n"
        string2=f"p2: (x: {self.vertices[1].x}, y: {self.vertices[1].y})\n"
        string3=f"p3: (x: {self.vertices[2].x}, y: {self.vertices[2].y})\n"
        string4=f"p4: (x: {self.vertices[3].x}, y: {self.vertices[3].y})\n"
        return string1+string2+string3+string4
    def area(self)->float:
        p1 =self.vertices[0]
        p2 =self.vertices[1]
        p3 =self.vertices[2]
        p4 =self.vertices[3]
        first_triangle =Triangle(p1,p2,p3)
        s1 = first_triangle.area()
        second_triangle=Triangle(p1,p2,p4)
        s2 = second_triangle.area()
        return s2
        
p1 = Point(0,0)
p2 = Point(2,2)
pl = Point(0,2)
p3 = Point(2,4)
p4 = Point(5,5)
d = Rectangle(p1,p2)
c = Triangle(p1,p2,pl)