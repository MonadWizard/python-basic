"""
It is a kind of class which we don't create an object. It is not instance at all
"""


class Animal:  # abstract class
    def move(self):  # empty method which is also abstract method
        pass


class Human(Animal):

    def move(self):
        print("I can Walk and run....")


class Snake(Animal):

    def move(self):
        print("I can crawl....")


def main():
    h1 = Human()
    h1.move()

    s1 = Snake()
    s1.move()


if __name__ == '__main__':
    main()
