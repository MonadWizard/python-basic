"""
class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
        self.msg = " \n this is message. "
    def print_exception(self):
        print("User define exception : ",self.msg)
    def handle(self):
        print("accident occer. take detour")
try:
    raise Accident('\n ::::::::::::::::  crash between two cars  ::::::::::::::: \n')
except Accident as e:
    e.print_exception()
    e.handle()
"""



def mathTest():
    import math

    nu = int(input("please enter the number : "))
    try:
        res = math.factorial(nu)
        print(res)                  #if we use negative value it face error

    #we can assign the type  of exception as it is ValueError
    except ValueError:
        print("cann't compute - value")
    #or
    except:
        print("can't compute negative : ")


def arithmeticError():    
    try:
        a = 10 / 0
        print(a)
    except ArithmeticError:
        print("face exception")
        print("""
        """)
    else:
        print("Welcome")


def finallyy():
    import math
    num = int(input("Enter input : "))
    try:
        res = math.factorial(num)
        print(res)
    except:
        print("yoou occer exception...")
    finally:
        print("good bye.....!")


def raiseEx():
    try:
        num = int(input("Enter a number : "))
        if num <=0:
            raise ValueError("this is not positive number")
    except ValueError as error:
        print(error)

raiseEx()
