"""
There are following in-built Type Functions:
min(tuple),   max(tuple),   len(tuple),     cmp(tuple1,tuple2),     tuple(sequence)
"""
from filecmp import cmp

data1=(101,981,1666,12,156,981,15)
data2=(101,981,'abcd','xyz','m')
data3=('aman','shekhar',100.45,98.2)
data4=(101,981,'abcd','xyz','m')




print("#### Tuple min(tuple)  : ")
print(min(data1))
#print(min(data3))   #face error cause it have string
print("""
""")




print("#### max(tuple)")
print(max(data1))
print("""
""")




print("#### len(tuple) : ")
print(data3)
print(len(data3))
print("""
""")




#print(cmp(data2,data3))............................................................fix cmp  not work..................




print("#### tuple(sequence) : ")
d3 = [10,20,30,40,50,60,70,80,90]
data = tuple(d3)
print(data)









