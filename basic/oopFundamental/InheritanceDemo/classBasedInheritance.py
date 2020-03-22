class Persion():  # parent class  which explecite object as parent class
# class Persion(object): # emplecite object as parent class

    def method1(self, a, b, c):
        self.var1 = a
        self.var2 = b
        self.var3 = c


class Employee(Persion):  # child class  or sub class
    pass


def main():
    obj1 = Persion()
    obj2 = Employee()

    obj1.method1(1, 2, 3)
    print(obj1.var1, obj1.var2, obj1.var3)

    obj2.method1(4, 5, 6)
    print(obj2.var1, obj2.var2, obj2.var3)

    # to see which class is sub-class. python use it's build in function "issubclass"
    print("Employee is a sub-class of Persion : ",
          issubclass(Employee, Persion))  # 1st parameter for child and 2nd for parents
    print("Persion is a sub-class of Employee : ", issubclass(Persion, Employee))
    print("Persion is a sub-class of object : ", issubclass(Persion, object))
    print("Employee is a sub-class of object : ", issubclass(Employee, object))


if __name__ == '__main__':
    main()
