"""
The "diamond problem" (sometimes referred to as the "deadly diamond of death") is the generally used term for an ambiguity
that arises when two classes B and C inherit from a superclass A, and another class D inherits from both B and C.
If there is a method "m" in A that B or C (or even both of them) )has overridden, and furthermore, if does not override this method,
then the question is which version of the method does D inherit? It could be the one from A, B or C

Let's look at Python. The first Diamond Problem configuration is like this: Both B and C override the method m of A:
"""


class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(B, C):
    pass


"""
If you call the method m on an instance x of D, i.e. x.m(), we will get the output "m of B called".
 If we transpose the order of the classes in the class header of D in "class D(C,B):", we will get the output "m of C called". 

The case in which m will be overridden only in one of the classes B or C, e.g. in C
"""

x = D()
x.m()   #Principially, two possibilities are imaginable: "m of C" or "m of A" could be used











