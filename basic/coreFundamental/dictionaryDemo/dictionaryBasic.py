"""
Dictionary is an unordered set of key and value pair. It is a container that contains data, enclosed within curly braces.
The pair i.e., key and value is known as item. The key passed in the item must be unique.
The key and the value is separated by a colon(:). This pair is known as item. Items are separated from each other by a comma(,).
Different items are enclosed within a curly brace and this forms Dictionary.
"""


data = {100: 'Ravi', 101: 'Vijay', 102: 'Rahul'}
print("data : \n", data)
print("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>""")



"""
Dictionary is mutable i.e., value can be updated.
Key must be unique and immutable. Value is accessed by key. Value can be updated while key cannot be changed.
Dictionary is known as Associative array since the Key works as Index and they are decided by the user.
"""


plant={}
print(plant)
plant[1]='Ravi'
plant['name']='Hari'
plant[2]='Manoj'
plant[4]='Om'
print(plant[2])
print(plant['name'])
print(plant[1])
print(plant)
print("""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")





data1 = {'Id':100, 'Name':'Suresh', 'Profession':'Developer'}
data2={'Id':101, 'Name':'Ramesh', 'Profession':'Trainer'}
print("Id of 1st employer is", data1['Id'])
print("Id of 2nd employer is", data2['Id'])
print("Name of 1st employer:", data1['Name'])
print("Profession of 2nd employer:", data2['Profession'])
print("""
""")

print("Value", data1['Id'])
print("Value", data1.get('Id'))
print("""
""")

print("KEYS", data1.keys())
print("VALUES", data1.values())

for a in data1:
    print("{f} ==>> {n}".format(f=a,n=data1[a]))

print("""
""")

print("""
................................................................................................""")
for key in data1:                                           #display total key and value serially
    print("On data1 => key:",key,"\t=> value:",data1[key])



print("""
print dictionary using 
      lambda fanction
""")


print(sorted(data1.items(), key = lambda t: t[0]))

print("""
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,""")




#### The item i.e., key-value pair can be updated. Updating means new item can be added. The values can be modified.
data1['Profession']='Manager'
data2['Salary']=20000
data1['Salary']=15000
print(data1)
print(data2)
print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")







x = 'Name' in data2    # it's search in value cause we define value in [].....if I give other than ['Name'] it face error..but why?????????????
print(x)
x1 = 'Name' in data2    # it's search in key caluse we define key freely , without[]
print(x1)

print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")

print(type(data1))
y = data1.clear()   #clean all data1 key_&_value
print(y)
print(type(y))
print(data1)     #data1.clear() make empty dictioary
print("""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")








#### del statement is used for performing deletion operation.
####An item can be deleted from a dictionary using the key only.
data={100:'Ram', 101:'Suraj', 102:'Alok'}
del data[102]
print(data)
del data
# print (data)   #will show an error since dictionary is deleted.  .............................................



# implementation different type of  Dictionary

my_set = {1,2,3}
my_dict = { 'name':'Rakib', 'age':24, 'gender':'male' }
another_dict = { 1:15, 2:30, 3:150 }

# tupple inside a dictionary
lottery_player = {
    'name': 'Rasid',
    'number': (13, 45, 66, 23, 22)
}

# dictionary inside a list
universities = [
    {
        'name': "DIU",
        'location': "Ashulia"
    },
    {
        'name': "MIT",
        'location': "US"
    }
    
]

# sum of lottery palyer
print("sum of lottery number: ",sum(lottery_player['number']))

# change the name of lottery palyer
lottery_player['name'] = 'Rouf'
# change the number of lottery palyer
lottery_player['number'] = (1,2,3,4,5,6)

print(lottery_player)





