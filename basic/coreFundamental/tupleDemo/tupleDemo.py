"""
Tuple is a list of values grouped together

List: All value have similar meaning (Homogeneous)
        Tuple:All values have different meaning(heterogeneous or homogeneous)
        Tuples are immutable
"""

"""
>>> p = (5,9)
>>> point[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'point' is not defined
>>> p[0]
5
>>> p[1]
9
>>> p[0]=50                                            #immutable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>> t = ((10,12.3),(3.5,5))
>>> t
((10,12.3),(3.5,5))
>>> t[0]
(10,12.3)
>>> t[0][0]
10

"""


def add_and_multiply(a, b):
    add = a + b
    multiply = a * b

    return add, multiply


n1 = int(input("Enter 1st number"))
n2 = int(input("Enter second number"))

total = add_and_multiply(n1, n2)

print(total)
