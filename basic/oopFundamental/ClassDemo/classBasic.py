"""
Major principles of object-oriented programming system are given below
>> Object      >>> Class       >>> Method     >>> Inheritance      >>> Polymorphism      >>> Data Abstraction       >>> Encapsulation
"""


class Point:  # define class
    pass  # if we don't want to use any variable or any method we can just use "pass". here "pass" is  initiation

class test1:     # this type of class is called an "empty class"
    pass         # create object then use by "object.variable" to define

# create an object
p1 = Point()

p1.x = 2
p1.y = 3
p1.z = 5

p2 = Point()

p2.a = 6
p2.b = 2
p2.c = -4

print("""
""")
print(p1)

print("dymantion of p1: ",p1.x,p1.y,p1.z)
print("dymantion of p2: ",p2.a,p2.b,p2.c)

print(p2)
print("""
""")


t1 = test1()
t1.text1 = "Hellow . I am totally f**ked up"
t1.tex2 = """
"""
t1.var1 = 45.2

print(t1.text1)
print(t1.var1)
print(t1.tex2)






class p:
    pass

p1 = p()
p1.x = 5
p1.y = 6
p1.z = 7
p1.threeD = (1,2,3,4,5,6)
print(p1)
print(p1.threeD)
print(p1.x,p1.y,p1.z)
print("""
""")


