my_veriable = ('hello')
my_list_variable =['hello','hi','nice to meet you']
my_tuple_variable = ('hello','hi','nice to meet you')
my_set_variable = {'hello','hi','nice to meet you'}


print(type(my_veriable))


print(f'list : {my_list_variable}')
print(f'tuple : {my_tuple_variable}') # can't modifi
print(f'set : {my_set_variable}')  # unorderd & removing duplicate

my_short_tuple_variable = ('hi',) # or can be use without 1st parenticise
print (my_short_tuple_variable)

#now print from list using subscript   name[index]
print(my_list_variable[:3])
print(my_tuple_variable[0])
#print(my_set_variable[2])  # can't support indexing

# add extra value
my_list_variable.append('another string') # . use to access it's left part by it's right part's operation
print(my_list_variable)

#my_tuple_variable.append('something') # tuple has no attribute 'append'
my_tuple_variable = my_tuple_variable + ('something',)
print(my_tuple_variable) 

my_set_variable.add('extra')
my_set_variable.add('hello') # can't duplicate
print(my_set_variable)
