"""This is Example of Abstract Factory Pattern in Python.
"""
import math

#Define Abstract classes. Alternatively, you can also define
class Shape2D:
    def area(self):
        pass

class Shape3D:
    def volume(self):
        pass

#---------------------------------------------------------------------------------#
#Abstract class ends here
#---------------------------------------------------------------------------------#

#Concrete classes for all 2D shapes

class Circle(Shape2D):
    def area(self, radius):
        self.area = math.pi*radius*radius
        return self.area

    def __repr__(self):
        return "Object is 2D circle object and area is {}".format(self.area)

class Square(Shape2D):
    def area(self, side):
        self.area = side**2
        return self.area

    def __repr__(self):
        return "Object is 2D suare object and area is {}".format(self.area)

class Rectangle(Shape2D):
    def area(self, length, width):
        self.area = length * width
        return self.area

    def __repr__(self):
        return "Object is 2D rectangle object and area is {}".format(self.area)

class Triangle(Shape2D):
    def area(self, base, height):
        self.area = 0.5 * base * height
        return self.area

    def __repr__(self):
        return "Object is 2D triangle object and area is {}".format(self.area)


#Concrete classes for all 3D shapes

class Sphere(Shape3D):
    def volume(self, radius):
        self.volume = (4/3)*math.pi*radius*radius*radius
        return self.volume

    def __repr__(self):
        return "Object is 3D sphere object and volume is {}".format(self.volume)

class Cube(Shape3D):
    def volume(self, side):
        self.volume = side**3
        return self.volume

    def __repr__(self):
        return "Object is 3D Cube object and volume is {}".format(self.volume)

class Box(Shape3D):
    def volume(self, length, width, height):
        self.volume = length * width * height
        return self.volume

    def __repr__(self):
        return "Object is 3D box object and volume is {}".format(self.volume)

class Pyramid(Shape3D):
    def volume(self, lenght, width, height):
        self.volume = 0.33333 * lenght * width * height
        return self.volume

    def __repr__(self):
        return "Object is 3D pyramid object and volume is {}".format(self.volume)



# Abstract Factory

class ObjectFactory:
    def get_object_measure(self,type,name):
        if type == "2D" and name == "circle":
            return Circle()
        if type == "2D" and name == "square":
            return Square()
        if type == "2D" and name == "rectangle":
            return Rectangle()
        if type == "2D" and name == "triangle":
            return Triangle
        if type == "3D" and name == "cube":
            return Cube()
        if type == "3D" and name == "sphere":
            return Sphere()
        if type == "3D" and name == "box":
            return Box()
        if type == "3D" and name == "pyramid":
            return Pyramid()

# main program start from here
def main():
    shapes = ObjectFactory()
    square = shapes.get_object_measure("2D","square")
    square.area(4)
    print(square)
    circle = shapes.get_object_measure("2D", "circle")
    circle.area(2)
    print(circle)
    cube = shapes.get_object_measure("3D","cube")
    cube.volume(4)
    print(cube)



main()


