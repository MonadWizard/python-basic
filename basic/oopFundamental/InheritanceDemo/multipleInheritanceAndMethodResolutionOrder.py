"""
when child class is derived from two or more parents is called multiple inheritance.

parent class      child class
classA         -> classC
classB         -> classC

"""


class A:

    def m(self):
        print("m() from A.........")


class B:

    def m(self):
        print("m() from B.........")


class C(A, B):  # multiple inheritance
    pass


def main():
    obj1 = C()  # obj1 first check on class C then if it not found then check on class A after that check class B. cause I define class A then class B in parameter
    obj1.m()


if __name__ == '__main__':
    main()
