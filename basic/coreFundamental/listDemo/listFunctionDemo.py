"""
function in list:
min(list),	max(list),  len(list),  cmp(list1,list2),   list(sequence)

"""
from msilib import sequence

list1=[101,981,1666,12,156,981,15]
list4=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
list3=[101,981,'abcd','xyz','m']

#### This method is used to get min value from the list.
print("min(list) : ")
print("Minimum value in List1: ",min(list1))
print("""
""")




#### This method is used to get max value from the list.
print("Maximum value in List : ",max(list1))
print("""
""")






#### This method is used to get length of the the list.
print("No. of elements in List1: ",len(list1))
print("""
""")






#### If elements are of the same type, perform the comparison and return the result.
#### If elements are different types, check whether they are numbers.
##### If numbers, perform comparison.
#### If either element is a number, then the other element is returned.
##### Otherwise, types are sorted alphabetically .
##### If we reached the end of one of the lists, the longer list is "larger." If both list are same it returns 0.

#print(cmp (list1,list2))

##....................................................................................fix cmp  not work...............




#### This method is used to form a list from the given sequence of elements.
print("#### list(sequence) : ")
sequence = (145, "abcd",'a')
data = list(sequence)
print("list formed is : " , data)





"""
There are following built-in methods of List:
index(object),  count(object),  pop()/pop(index),   insert(index,object),   extend(sequence),   remove(object),
reverse(),  sort()
"""

print(" #### index() ")
print("Index of 12 is " , list1.index(12))




print("#### count(object) ")
print("Number of time 981 occured is : ",list1.count(981))





print("#### pop()/pop(int) ")
print("Last element is : ",list1.pop())
print("2nd position element : ",list1.pop(1))
print(list1)




print("#### insert(index,object) : ")
list2.insert(2,"hello")
print(list2)




print(" extend(sequence) : ")
list2.extend(list3)
print("list2 : ",list2)
print("list3 : ",list3)




print("#### remove(object) : ")
print("list2 : ",list2 )
list2.remove("hello")
print("list2 : ",list2)



print("#### reverse() : ")
print("list1",list1)
list1.reverse()
print("list1 : ",list1)




print("#####  sort() : ")
list1.sort()
print("list1 : ",list1)





