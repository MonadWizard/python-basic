"""
Method need "self" reference paramenet  but function don't need self reference parameter
"""







def a(x,y):
    return x*y

class Point3:


    def assign(self,x ,y, z):   #method
        self.a = x
        self.b = y
        self.c = z


    def printPoint(self):
        print(self.a, self.b,self.c) # method
        print(a(self.a,self.b))          #use a function on printPoint method



# using method :
p1 = Point3()
p1.assign(2, 3, 5)
p1.printPoint()




# without method or function:
p1 = Point3()

p1.a = 2
p1.b = 3
p1.c = 4

print(p1.a,p1.b,p1.c)

