"""
Polymorphism - The ability to assume various forms.

Overriding is a type of polymorphism.

overriding is when you call a method on an object and the method in the subclass with the same signature
as the one in the superclass is called.

Method overriding is an object-oriented programming feature that allow a subclass to provide a different implementation of a
method that is already defined by its superclass or by one of its superclass

Super Resurved keyWord is call to initial parent class
"""


class Persion:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + " " + self.last + ", " + str(self.age)


class Employee(Persion):  # inharite Persion

    def __init__(self, first, last, age,salary):  # overriding
        # self.first = first
        # self.last = last
        # self.age = age
        super().__init__(first,last,age)  # super keyword call Persion class's __init__ method
        self.salary = salary

    def __str__(self):  # override
        return super().__str__() + " , "+ str(self.salary)
        # return self.first + " " + self.last + ", " + str(self.age) + ", " + str(self.salary)



def main():
    x = Persion("Rakib Hasan", "Rakib", 31)
    print(x)

    # y = Employee("All", "People", 30)
    # print(y)

    y1 = Employee("All", "People", 30, 500000)
    print(y1)


if __name__ == '__main__':
    main()
