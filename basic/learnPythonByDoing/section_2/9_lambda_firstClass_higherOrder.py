def add_tow(x, y):
    return x + y

add_tow(5, 10)


# annonimous function or lambda function..........
lambda x, y: x+y   # here we define x, y and then just return using : and return x+y
# lambda function can't work without initial it with variable. and python distroy unused script to incress parfamrnts. so,
a = (lambda x, y: x+y)(10,50)
print(a)


# function with dictionary
def who (data, identify):
    return identify(data) # here identify is a function parse by parameter 

def my_identify_function(some_data):
    return some_data['name']


user = {'name' : 'Rakib Hasan','surname' : 'dust!nk'}
print(who(user, my_identify_function))


# we can work same as my_identify_function with lambda function
print(who(user, lambda x: x['name']))


print(my_identify_function({'name' : 'Rakib'}))



#.......................................need to be seen tutorial again...21





