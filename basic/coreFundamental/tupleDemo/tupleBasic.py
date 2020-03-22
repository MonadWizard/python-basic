"""
A tuple is a sequence of immutable objects, therefore tuple cannot be changed. It can be used to collect different types of object.
The objects are enclosed within parenthesis and separated by comma.
Tuple is similar to list. Only the difference is that list is enclosed between square bracket, tuple between parenthesis and
List has mutable objects whereas Tuple has immutable objects.
"""

data1=(101,981,1666,12,156,981,15)
data2=(101,981,'abcd','xyz','m')
data3=('aman','shekhar',100.45,98.2)
data4=(101,981,'abcd','xyz','m')

print(data1)
print(data2)


####   There can be an empty Tuple also which contains no object. Lets see an example of empty tuple.
data5 = ()
print(data5)
print("""
""")


#### For a single valued tuple, there must be a comma at the end of the value.
data6 = (10,)
print(data6)
print("""
""")



#### Tuples can also be nested, it means we can pass tuple as an element to create a new tuple.
print("data1 : ",data1)
data7 = data1,(10,20,30,40)
print("data1 : ",data1)
print("data7 : ",data7)
print("""
""")




print("#### Accessing Tuple : ")
print("data2 : ",data2)
print(data2[0])
print(data2[0:2])
print(data2[-3:-1])
print(data2[0:])
print(data2[:2])
print("""
""")



print("#### Elements in a Tuple : ")
data=(1,2,3,4,5,10,19,17)
print(data)
print("""Data[0]=1=Data[-8] , Data[1]=2=Data[-7] , Data[2]=3=Data[-6] , 
Data[3]=4=Data[-5] , Data[4]=5=Data[-4] , Data[5]=10=Data[-3],  
Data[6]=19=Data[-2],Data[7]=17=Data[-1] """)
print("""
""")




#### Tuple can be added by using the concatenation operator(+) to join two tuples.
print("data2 : ",data2)
print("data3 : ",data3)
print((data2 + data3))
print("""
""")




#### repeating can be performed by using '*' operator by a specific number of time.
print("data2 : ",data2)
print("data2 * 2", (data2*2))
print("data3 : ",data3)
print("data3 * 3 : ", data3*3)
print("""
""")






#### A subpart of a tuple can be retrieved on the basis of index. This subpart is known as tuple slice.

print (data1[0:2])
print (data1[4])
print (data1[:-1])
print (data1[-5:])
print (data1)
print("""
""")





#### We can create a new tuple by assigning the existing tuple.
print(data3)
print(data4)
print(data3+data4)
print("""
""")



del data3
#print(data3)  #this tuple was deleted so seen error







