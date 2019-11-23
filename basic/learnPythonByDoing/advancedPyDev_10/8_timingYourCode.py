import time

# find executing time
def power(limit):
    return [x**2 for x in range(limit)]

start = time.time()

p = power(50000)

end = time.time()

print(start - end)



#or we can do with lambda to execute runTime
def measure_time(func):
    
    startt = time.time()
    func()
    endd = time.time()
    print(endd - startt)
    
measure_time(lambda: power(50000))


# we can execute littel pice of code using timeit
import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))    # LIST COMPREHENTION
# also work same with lambda
print(timeit.timeit("map(lambda x: x**2, range(10))"))   # MAP TAKE LESS TIME THAN LIST COMPREHENTION








