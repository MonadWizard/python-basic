"""
python function :
len(dictionary),    cmp(dictionary1,dictionary2),    str(dictionary)
python method :
keys(),    values(),    items(),    update(dictionary2),    clear(),    fromkeys(sequence,value1)/ fromkeys(sequence)
copy(),     get(key)
"""

data = {100: 'Ram', 101: 'Suraj', 102: 'Alok'}
data1 = {100: 'Ram', 101: 'Suraj', 102: 'Alok'}
data2 = {103: 'abc', 104: 'xyz', 105: 'mno'}
data3 = {'Id': 10, 'First': 'Aman', 'Second': 'Sharma'}
data4 = {100: 'Ram', 101: 'Suraj', 102: 'Alok'}

print("######## It returns length of the dictionary.")
print("#### len(dictionary) : ")
print(data)
print(len(data))
print("""
""")

print("##### cmp(dictionary1,dictionary2) : ")
# print (cmp(data1,data2)).....................................................................................
print("here some problem.")
print("""
""")

print("######## This method returns string formation of the value.")
print("#### str(dictionary) :")
print(str(data1))
print("""
""")

print("######## This method returns all the keys element of a dictionary.")
print("#### keys() : ")
print(data1.keys())
print("""
""")

print("######## This method returns all the values element of a dictionary.")
print("#### values() : ")
print(data1.values())
print("""
""")

print("######## This method returns all the items(key-value pair) of a dictionary.")
print("#### items()  : ")
print(data1.items())
print("""
""")

print("######## This method is used to add items of dictionary2 to first dictionary.")
print("#### update(dictionary2) : ")
data1.update(data2)
print(data1)
print(data2)
print("""
""")

print("####### It returns an ordered copy of the data.")
print("#### clear() : ")
print(data3)
data3.clear()
print(data3)
print("""
""")

print("""######### This method is used to create a new dictionary from the sequence where sequence elements forms the key
# and all keys share the values ?value1?.
#########  In case value1 is not give, it set the values of keys to be none.
""")
print("#### fromkeys(sequence)/ fromkeys(seq,value) : ")
sequence = {'id', 'name', 'email', 'extra'}
data3 = data3.fromkeys(sequence)
print(data3)
data3 = data3.fromkeys(sequence, 100)
print(data3)
print("""
""")

print("######## This method returns an ordered copy of the data.")
print("#### copy() : ")
print(data3)
print(data1)
data3 = data1.copy()
print(data3)
print("""
""")

print("######### It returns a boolean value. True in case if key is present in the dictionary, else false.")
print("#### has_key(key) : ")
# print (data.has_key('Age')) #............................................................. show error , solve it......


print("####### This method returns the value of the given key. If key is not present it returns none.")
print("#### get(key) : ")
print(data3.get(100))
print(data3.get("votka"))
