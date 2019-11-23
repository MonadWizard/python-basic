# map syntex :      map(function, itteration)


num = [1,2,3,4]
def square(a):
    return a**2
print('square{numb}'.format(numb = map(square, num)))    # print map object
#we need to convert map obj to list or tupple to use
print('square{numb}'.format(numb = list(map(square, num))))




# now we work with lambda function 
num = [1,2,3,4]
print('square{numb}'.format(numb = list(map(lambda x: x**2 , num))))


# using lambda square 1 to 9 in list

print([(lambda x: x*x)(x) for x in range(10)])




# now we work with list comprehention  syntex      [operation for operation_value in object]
num = [1,2,3,4]
print('square{numb}'.format(numb = [x**2 for x in num] ))
 



# find length of string in list 

name = ['Rakib', 'Dust_ink', 'monad_wizard', 'amonaly_careleess']
print([x for x in map(len, name)])   # map obj ta only 1 bar loop chola
print([x for x in name[:]])





















############### danger ##########
"""
n = [1,2,3,4]
for num in n:
    n.append(num)
    #print(n)   # infinity loop

"""

