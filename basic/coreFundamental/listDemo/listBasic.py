data1=[1,2,3,4]
data2=['x','y','z']

print (data1[0])
print (data1[0:2])  # list(start, end+1)
print (data2[-3:-1])
print (data1[0:])
print (data2[:2])
print("""
""")




#### lists can be added by using the concatenation operator(+) to join two lists.
list1 = data1 + data2
print("add data1 + data2 ",list1)
print("""
""")

#### Replicating means repeating, It can be performed by using '*' operator by a specific number of time.
print("data1 * 5 : \n", data1*5)
print("""
""")

a = []
for i in data1:
    a.append(i*5)
    
    print(i)

print(a)


#### A subpart of a list can be retrieved on the basis of index. This subpart is known as list slice.
#### This feature allows us to get sub-list of specified start and end index.
print (list1[0:2])
print (list1[4])
list1[1]=9
print (list1)
print("""
""")





#### To update or change the value of particular index of a list, assign the value to that particular index of the List.
data1[2]="Multiple of 5"
print("Values of list are: ",data1 )
print("""
""")




#### Python provides, append() method which is used to append i.e., add an element at the end of the existing elements.
data1.append(253.13)
print("append 253.13 to data1 : ",data1)
print("""
""")


####bIn Python, del statement can be used to delete an element from the list.
#### It can also be used to delete all items from startIndex to endIndex.
print("data1 : ",data1)
del data1[3]
print("del data1[3]",data1)
del data1[0:3]
print("del list[0:3] : ",data1)




a = [1,2,3,4]
a.append(10)
print(a)





