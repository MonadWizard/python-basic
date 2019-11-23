"""
hybrid Inheritance is one kind of multilevel inheritance

parent class    child class
Class A         -> Class B
Class A         -> Class C
Class C         -> Class D
Class B         -> Class D
"""

class A:

    def m(self):
        print("m() from class A...")

class B(A):

    def m(self):
        print("m() from class B")
        A.m(self)    # override

class C(A):

    def m(self):
        print("m() from class C")
        A.m(self)

class D(B,C):

    def m(self):
        print("m() from class D...")

        super().m()

        # B.m(self)
        # C.m(self)
        # A.m(self)

def main():
    obj1 = D()
    obj1.m()

if __name__ == '__main__':
    main()
