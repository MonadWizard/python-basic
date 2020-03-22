"""
target
find the dimension of the array
find the byte size of each element
find the data type of the element
"""

import numpy as np

a = np.array([(1,2,3,4,5),(6,7,4,5,6),(1,2,7,8,9)])
a1 = np.array([(1,2,3),(4,5,6),(7,8)])  # ............................?
a2 = np.array(['a','s','d'])

print(a.ndim)  # ndim give the dimantion of array
print(a1.ndim)
print(a2.ndim)

print("""
---------------------size--------------------------------------------
""")
print(a.size)  # size give total amount of element are execute
print(a1.size)
print(a2.size)

print("""
-------------------------dtype-----------------------------------------
""")
print(a.dtype) # dtype give the datatype of element
print("a1",a1.dtype)
print("a2",a2.dtype)

print("""
-----------------------shape--------------------------------------------
""")
print(a.shape)  # shape represent size of row than size of column
print(a1.shape)
print(a2.shape)


"""
now see reshaping array. it means make rows to column and make column as row
"""
print("""
----------------------------------reshape-----------------------------
""")
print(a,"""
""")
a = a.reshape(5,3)
print(a)



"""
now see slaiseing . it means extract particular set of element from array
"""
print("""
-------------------------------slaysing----------------------------------
""")
aa = np.array([(1,2,3,4,5),(6,7,4,5,6),(1,2,7,8,9)])

print(aa[0, 2])  # arrayName[dimentionNumber , indexOfElement]

print(aa[0:, 3])  # arrayName[dimentionNumber : , indexOfElement]       :  means all dimention include define

print(aa[0:2, 3])  # arrayName[startDimention : toBeforEndDimention , indexOfElement]


print("""
-----------------------------------linespace--------------------------------
""")
aa2 = np.linspace(1,3,20)  # linspace(startNumber,lastLimit,totalNumberMake
print(aa2)


print("""
------------------------------------max---------------------------------------
""")
ab = [1,2,3,4,5,6,7,8,9]
print(max(ab))

print("""
------------------------------------min---------------------------------------
""")
print(min(ab))

print("""
------------------------------------sum---------------------------------------
""")
print(sum(ab))

print("""
------------------------------------X - axis-----------------------------------------
""")
print(a.sum(axis = 0))  # axis = 0 means row


print("""
------------------------------------Y - axis-----------------------------------------
""")
print(a.sum(axis = 1))  # axis = 1 means column


print("""
-----------------------------------squire root ---------------------------------------
""")
print(np.sqrt(a))  # sqrt(arrayName) for squire root of total row


print("""
------------------------------------- standerd divition --------------------------------
""")
print(np.std(a))


print("""
------------------------------------arithmatic operation---------------------------------
""")
b = np.array([(1,2,3,4,5),(6,7,4,5,6),(1,2,7,8,9)])
print("a+b", (aa+b))
print("a-b", (aa-b))
print("a*b", (aa*b))
print("a/b", (aa/b))


print("""
----------------------------------concatination array-------------------------------------
as vartically or horizontally
""")
print("vartically stack :\n", np.vstack((aa,b)))  # vstack  can concatinate or stack as vartically
print("\n horizontally stack :\n", np.hstack((aa,b)))  # hstack  can concatinate or stack as horizontally



print("""
------------------------------in single column---------------------------------------------
""")
print(b.ravel())  # print all separate array dimention on single column
















