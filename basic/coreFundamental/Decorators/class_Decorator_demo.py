# __call__ dunder method............................................
class Printing:
    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print("enter user name is : ", self.name)

p = Printing("Rakib")
p()


# simple decorator......................................................

def decorator(f):
    def inner():
        str1 = f()
        return str1.upper()
    return inner

@decorator
def greet():
    return "good work"

print(greet.__name__)


# change object referance decorator to function.........................
import functools
def decorator(f):
    @functools.wraps(f)
    def inner():
        str1 = f()
        return str1.upper()
    return inner

@decorator
def greet():
    return "good work"

print(greet.__name__)


# use outer decorator inside a class...........................
def check_name(method):
    def inner(name_ref):
        if name_ref.name == "Rakib":
            print("Hey my name is also same!!!")
        else:
            method(name_ref)
    return inner


class Printing:
    def __init__(self,name):
        self.name = name
    @check_name    
    def print_name(self):
        print("enter user name is : ", self.name)
p = Printing("Rakib")
p.print_name()


#----------------------------------- class decorator --------------------------

class Decorator:
    def __init__(self,func):
        self.func = func
        
    def __call__(self):
        str1 = self.func()
        return str1.upper()

@Decorator
def greet():
    return "good work"

print(greet())



# another example

class Check_div:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        l = []
        l = args[1:]
        for i in l:    
            if i == 0:
                return "You can't devide use non-zero value "
            else:
                self.func(*args)

@Check_div
def div(a,b):
    return a/b
@Check_div
def divv(a,b,c):
    return a/b/c


print(div(10,0))
print(divv(1,0,1))



































