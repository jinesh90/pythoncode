"""
Prototype pattern is used when Object is heavy weighted.
Example Making Connection to Network and Connect.Prototype Pattern is related to
clone object

"""

from copy import deepcopy

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("Point ({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        obj = deepcopy(self)
        obj.move(move_x, move_y)
        return obj



def main():
    p0 = Point(0,0)
    print(p0)
    # now if user wants to create another point without instantiate another object then
    p1 = p0.clone(1,3)
    print(p1)


main()