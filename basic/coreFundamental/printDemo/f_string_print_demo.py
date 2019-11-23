a = 'Rakib'
b = 'Hasan'

print('My name is {} {}'.format(a,b))
 
# or
print(f'My name is {a} {b}') 

# or
print(f'My name is {a.upper()} {b.lower()}') 


# with dictionart
person= {'name': 'Rakib', 'age': 23}
print('My name is {name} and I\'m {age} years old'.format(name= person['name'], age= person['age']))
# or
print(f"My name is {person['name']} and I\'m {person['age']} years old" )


#with loop
b = 0
for a in range(1,10,2):
    b += 1
    print("1 to 10 by {first}st deference is {difference:02.3f}".format( first= b , difference = a))
    print(f"The value with 3 decemel number is {a:03.2f}")


# with enumerate function

for b, a in enumerate(range(1,10,2)):
    print("1 to 10 by {first}st deference is {difference:02.3f}".format( first= b , difference = a))




# with date time
from datetime import datetime

d = datetime(1999,2,21) #year, month, date
print(d)
print(f'{d:%B %d, %y}')

