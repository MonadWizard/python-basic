"""
when some classes are roll as parents and child both type of class   and there are one class can roll only parents class
and one class is roll as only child class is called multilevel inheritance.

parent class     child class
classA        ->  classB
classB        ->  classC
classB is child and parent both type of class.
"""


class Persion:

    def assign(self, name, age):
        self.name = name
        self.age = age


class Employee(Persion):

    def assigEmp(self, idno):
        self.id = idno


class Programmer(Employee):

    def assignProg(self, lang):
        self.lang = lang


def main():
    obj1 = Programmer()
    obj1.assign("Rakib", 31)
    obj1.assigEmp(1002)
    obj1.assignProg("Python 3")
    print(obj1.name, obj1.age, obj1.id, obj1.lang)


if __name__ == '__main__':
    main()
