# create dynamic list 
list_2 = [x for x in range(5)]
print(list_2)

# create a list 5 to 10 by difference 2
list_1 = [x for x in range(5,10,2)]
print(list_1)

# create a list only even value 0 to 5
even_list = [x for x in range(5) if x%2 == 0 ] 
print(even_list)


# normalize list in lower case
people = ['Rouf', 'Ana', 'Rakib', 'Rasid']
lower = [p.strip().lower() for p in people ]
print(lower)



