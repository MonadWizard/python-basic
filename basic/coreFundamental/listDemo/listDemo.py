'''
>>> list1 = [1,2,3,4,5,6,7,8,9,0]
>>> list1[3]
4
>>> list1[4] = 12
>>> list
<class 'list'>
>>> list1
[1, 2, 3, 4, 12, 6, 7, 8, 9, 0]
>>> list1.insert(2,'hello')
>>> list1
[1, 2, 'hello', 3, 4, 12, 6, 7, 8, 9, 0]
>>> list1.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> list2 = ["sc",'sd',"sfa",'wewq',"ty","ada"]
>>> list2.sort()
>>> print(list2.sort())
None
>>>
>>>
>>> list2
['ada', 'sc', 'sd', 'sfa', 'ty', 'wewq']
>>> l3 = [1,2,4,46,64,86,464,846,186,4,54]
>>> l3.sort()
>>> l3
[1, 2, 4, 4, 46, 54, 64, 86, 186, 464, 846]
>>>
>>> del l3[5]
>>> l3
[1, 2, 4, 4, 46, 64, 86, 186, 464, 846]
>>>
>>> del l3
>>> l3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l3' is not defined
>>>
>>>
>>> list1.append("sfaa")
>>> list1
[1, 2, 'hello', 3, 4, 12, 6, 7, 8, 9, 0, 'sfaa']
>>>
>>>
>>> list1.reverse()
>>> list1
['sfaa', 0, 9, 8, 7, 6, 12, 4, 3, 'hello', 2, 1]
>>>
'''

print("First list \n")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(l)

print("replace : ")
l[3] = "rakib"  # replace
print(l)

print("insert : ")
l.insert(5, "Hasan")  # insert
print(l)

print("create : ")
l2 = ["fas", "eawf", "Eawf", "aewf"]  # create
print(l2)

print("sort by assending : ")
l2.sort()  # sort by assending
print(l2)

print("delete : ")
del l[3]  # delete
print(l)

print("delete total list l ")
del l  # delete total list

print("append : ")
l2.append("what")  # append
print(l2)

print("reverse : ")
l2.reverse()  # reverse
print(l2)
