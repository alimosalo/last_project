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
    def length(self):
        return sqrt(self.x**2 + self.y**2)       

class Shape:
    def __init__(self) -> None:
        self.vertices=[]
        
    def add_vertex(self,p:Point):
        self.vertices.append(p)
    def __repr__(self):
        return "Shape()"
    def __str__(self):
        return f"number of vertices: {len(self.vertices)}"
    def perimeter(self):
        if len(self.vertices)==0:
            raise RuntimeError
        side_pos=[]
        side_len=[]
        position = self.vertices[0]
        #finding vector of each side 
        for i in self.vertices[1:]:
            side_pos.append(position-i)
            position = i 
        if len(self.vertices)>=3:
            side_pos.append(self.vertices[-1]-self.vertices[0])
        # calculating the length of each side
        for i in side_pos:
            l = sqrt(i.x**2+i.y**2)
            side_len.append(l)
        return sum(side_len)
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
        if p1.x==p2.x==p3.x or p1.y==p2.y==p3.y:
            raise RuntimeError
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
        return abs(s)
##class Rectangle ####
class Rectangle(Shape):
    def __init__(self,p1,p2) -> None:
        super().__init__()
        p3 = Point(p2.x,p1.y)
        p4 = Point(p1.x,p2.y)
        self.add_vertex(p1)
        self.add_vertex(p3)
        self.add_vertex(p2)
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
        first_triangle =Triangle(p1,p3,p2)
        s1 = first_triangle.area()
        second_triangle=Triangle(p2,p4,p1)
        s2 = second_triangle.area()
        return s1+s2
        
# p1 = Point(1,1)
# p2 = Point(2,4)
# pl = Point(0,2)
# p3 = Point(2,4)
# p4 = Point(5,5)
# d = Rectangle(p1,p2)
# c = Triangle(p1,p2,pl)
# d.perimeter()
# print(d)
# print(d.perimeter())