"""
there are 10 type of sequences in string , lst , tuple
*LENGTH  *SELECT *SLICE *COUNT *INDEX *MEMBERSHIP  *CONCATENATION *MIN VALUE *SUM
"""
'''
>>>
>>> name = "Rakib"
>>> list1 = [12,123.4,56,6.8]
>>> tuple1 = (10,2.4,5.8,5)
>>>
>>> len(name)
5
>>> len(list1)
4
>>> len(tuple1)
4
>>> name[0]
'R'
>>> list[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> list1[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> list1[2]
56
>>> tuple1[2]
5.8
>>>
>>>
>>> name[1:4]
'aki'
>>>
>>> list1[1,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> list1[1:3]
[123.4, 56]
>>> tuple1[1:3]
(2.4, 5.8)
>>>
>>>
>>> list1[1:]
[123.4, 56, 6.8]
>>> list1[:2]
[12, 123.4]
>>>
>>>
>>> list1.countu('m')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'countu'
>>> list1.countu('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'countu'
>>> list1.count('a')
0
>>> name.count('a')
1
>>> list1.count('2')
0
>>> name.index('k')
2
>>>
>>>

'''






