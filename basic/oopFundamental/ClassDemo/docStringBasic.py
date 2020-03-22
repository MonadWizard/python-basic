"""
we can use documentation on python code .
It's called docstring.
"""

'This is a docstring section for this file but execute 1st one .'


class Point:
    'This is a docstring for class point'

    def __init__(self, x, y, z):
        'This is initializer method for class Point'
        'This isn\'t seen as docString cause docString execute first one'
        self.assign(x, y, z)

    def assign(self, x, y, z):
        'This method assigns the value to the co-orderind of point'
        self.a = x
        self.b = y
        self.c = z

    def printPoint(self):
        'This method point the values to the co-ordinates of point'
        print(self.a, self.b, self.c)


print("docString on code : ", __doc__)
p1 = Point(0, 0, 0)
print("docString on class : \n", p1.__doc__)
print("docString on __init__ \n: ", p1.__init__.__doc__)
print("docString on assign : \n", p1.assign.__doc__)
print("docString on printPoint \n: ", p1.printPoint.__doc__)
print("""

""")



#################help method gives us method with docString to seen all summary in short time
print("print help(class)",help(p1))
print("\n         help on assign method : \n")
print(help(p1.assign))
