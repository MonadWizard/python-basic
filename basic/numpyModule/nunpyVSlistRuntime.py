"""
Numpy is the core library for scientific computing in python.
It provides a high-performance multi dimensional array object, and tools for working with these arrays.
1 row means 1 dimensional .
"""

import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])

print(a)

"""
>>> np.array([1, 2, 3])
array([1, 2, 3])
Upcasting:
>>> np.array([1, 2, 3.0])
array([ 1.,  2.,  3.])
More than one dimension:
>>> np.array([[1, 2], [3, 4]])
array([[1, 2],
       [3, 4]])
Minimum dimensions 2:
>>> np.array([1, 2, 3], ndmin=2)
array([[1, 2, 3]])
Type provided:
>>> np.array([1, 2, 3], dtype=complex)
array([ 1.+0.j,  2.+0.j,  3.+0.j])
Data-type consisting of more than one element:
>>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
>>> x['a']
array([1, 3])
Creating an array from sub-classes:
>>> np.array(np.mat('1 2; 3 4'))
array([[1, 2],
       [3, 4]])
>>> np.array(np.mat('1 2; 3 4'), subok=True)
matrix([[1, 2],
        [3, 4]])
"""

print("""


""")

"why we use numpy if we have list"
"""
WE USE NUMPY FOR:
1. it's use less memory than list
2. it's mush fast when we compare it with list
3. very Convenient (সুবিধাজনক)
"""

import time
import sys

s = range(1000)  # range give all int value between 1-1000.

print(sys.getsizeof(5) * len(s))  # getsizeof(anyOneElement)*len(list) this give the memory space of list
# sys.getsizeof give the memory size and multiply by list give total list memory size


# now work same with numpy array

"""
>>> np.arange(3)
array([0, 1, 2])
>>> np.arange(3.0)
array([ 0.,  1.,  2.])
>>> np.arange(3,7)
array([3, 4, 5, 6])
>>> np.arange(3,7,2)
array([3, 5])
"""
D = np.arange(1000)
print(D.size*D.itemsize)


print("""
------------------------------------------------------------
""")


# now see more clearly

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)] # use for loop to run total amount of SIZE

print((time.time() - start) * 1000) # define 1000 for convert in mili-seconds

# for numpy
start = time.time()
result2 = A1 + A2

print((time.time() - start) * 1000) # define 1000 for convert in mili-seconds

























