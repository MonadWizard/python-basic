"""
when a parents class inherit to multiple child classes , it's called  Hirerachical inheritance

parents class          child class
Animal           ->    Human
                 ->    Fish
"""


class Animal:

    def move(self):
        print("I move therefore I can.....")


class Human(Animal):

    def move(self):
        print("Human can walk and run.......")


class Fish(Animal):

    def move(self):
        print("fish can swim and dive.......")


def main():
    h1 = Human()
    h1.move()

    f1 = Fish()
    f1.move()

if __name__ == "__main__":
    main()