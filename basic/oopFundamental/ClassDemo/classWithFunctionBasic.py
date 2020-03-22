def sum(a, b):  # function
    c = (a + b)
    print("sum function : ", c)


def fun1(a, b):  # function
    return int(a + b)


class Point2:

    def assign(self, a, b, c):  # method
        self.x = a  # self.x is the variable in the class point and x is the parameter
        self.y = b
        self.z = c
        print("use fun function on assign method : \n", "static : ", fun1(5, 9), "\n dynamic : ", fun1(self.x, self.z))

    def printPoint(self):  # method
        print("print assign method's parameter passed value : ", self.x, self.y, self.z)
        print("sum function define on pintPoint method : ", sum(self.x, self.y))  ####run function inside method
        print("sum function define on pintPoint method : ", sum(4,2))
        print("fun function diclar on printPoint method : ", fun1(self.y, self.z))


# work without method :
p1 = Point2()
p1.x = 2
p1.y = 7
p1.z = 5

p1.assign(p1.x, p1.y, p1.z)
p1.printPoint()

print("without method", p1.x, p1.y, p1.z)

sum(3, 5)  # define sum function without method
