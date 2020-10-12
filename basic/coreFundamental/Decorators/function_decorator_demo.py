# simple Decorator
def st_upper(x):
    def inner():
        y = x()
        return y.upper()
    return inner

@st_upper
def print_str():
    return "good work"

print(print_str())



#--------------------------- function with parameter Decorator ---------------------------

def zero_dev_err(d):
    def inner(x,y):
        if y == 0:
            return("plz put nonZero to 2nd number")
        return d(x,y)
    return inner


@zero_dev_err
def divv(a, b):
    return a/b

print(divv(4,0))


#--------------------------- Multiple Decorators in single Function ---------------------------
def upper_f(func):
    def inner():
        srt1 = func()
        return srt1.upper()
    return inner

def split_f(func):
    def inner():
        str2 = func()
        return str2.split()
    return inner

# first it apply immidet upper decorator then 2nd immidet upper decorator
@split_f
@upper_f
def str_func():
    return "good work"

print(str_func())


# see how decorators work...........................................

def upper_f(func):
    def inner():
        return "1st" , func() , "first"
    return inner

def split_f(func):
    def inner():
        return "2nd" , func() , "second"
    return inner

# first it apply immidet upper decorator then 2nd immidet upper decorator
@split_f
@upper_f
def str_func():
    return "good work"

print(str_func())


#--------------------------- Decorators with parameters ---------------------------

def outer_f(expr):
    def upper_f(func):
        def inner():   
            return func() + expr
        return inner
    return upper_f
    
@outer_f("Rakib")
def str_func():
    return "good work "

print(str_func())



#--------------------------- Single Decorator in multi function --------------------------- 
# General Decorator

def zero_dev_err(d):
    def inner(*args):
        l1 = []
        l1 = args[1:]
        for i in l1:
            if i == 0:
                return("plz put nonZero to 2nd number")
        return d(*args)
    return inner


@zero_dev_err
def divv(a, b):
    return a/b

@zero_dev_err
def divvvv(a,b,c,d):
    return a/b/c/d

print(divv(4,1))

print(divvvv(4,2,0,2))




















