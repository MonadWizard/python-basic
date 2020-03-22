number = list(range(10)) # range work same as for in list
print(number)

double_numbers = []
for num in number:
    double_numbers.append(num * 2)
print(double_numbers)

#make same by comprehension
double_number = [n*2 for n in number]
print(double_number)

# another list comprehension
phrase = [f'I am {age} years old.  ' for age in number]
print(phrase)

# another list comprehension lowercase
name_list = ['Rakib', 'Rasid', 'Akfa', 'Rauf']
lowercase_names = [name.lower() for name in name_list]
print("""
      """, lowercase_names)
friend = input('Enter a name: ')
print(friend.lower() in lowercase_names)
print(friend in lowercase_names)


# With conditional store even number
even = [n for n in number if n % 2 == 0]
print(even)

print("""
      """)

friends = ['f1','f2','f3','f4']
guest = ['f','f2','f6','f3','f9']

present_friends = [name for name in friends if name in guest]
print(present_friends)



friendz = ['f1','f2','f3','f4']
guestz = ['f','F2','f6','F3','f9']

present_friendz = [name.lower() for name in friendz if name.capitalize() in guestz]
print(present_friendz)


friendzzz = ['f1','f2','f3','F4']
guestzzz = ['f4','F2','f6','F3','f9']

lower_friends = [n.lower() for n in friendzzz]
present_friendzzz = [name.capitalize() for name in guestzzz if name.lower() in lower_friends]
print(present_friendzzz)


friendzz = ['f1','f2','f3','F4']
guestzz = ['f4','F2','f6','F3','f9']

present_friendzz = [name.capitalize() for name in guestzz if name.lower() in [n.lower() for n in friendzz]]
print(present_friendzz)


