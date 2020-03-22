"""
initilizer Method is likely constractor on C++ or Java . But It's not constractor in python
"""


class Point2:

    def __init__(self, x, y, z):
        self.printPoint2(x, y, z)
        self.assign(x, y, z)

    def printPoint2(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
        print("printPoint2 : ", int((self.a + self.b + self.c)))

    def assign(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
        print(self.x, self.y, self.z)

    def printPoint(self):
        print(self.a, self.b, self.c)


p1 = Point2(2, 7, 5)  # this value is pass to __init__(parameter)
p2 = Point2(5, 6, 8)

p1.printPoint()
p2.printPoint()