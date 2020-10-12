def outer():
    x = 5
    def inner():
        y = 3 * x
        result = x + y
        return result
    return inner

a = outer()

# see what a represent
print(a.__name__)

print(a()) 


########################################################
def print_upper(x):
    def inner():
        y = x()
        return y.upper()
    return inner

def print_str():
    return "good work"

upp = print_upper(print_str)
print(upp.__name__)
print(upp())
