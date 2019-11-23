#square={1:1, 2:4, 3:9}
square = {num:num**2 for num in range(1,11)}
print(square)


# square of 1 is 1
square ={f'square of {num} is':num**2 for num in range(1,11) }
print(square)

# print seperetly
square ={f'square of {num} is':num**2 for num in range(1,11) }
for k,v in square.items():
    print(f'square of {k} is {v}')


# check how many time a caracter exists is string
str= 'I am Dust ink'
word_count = {charect : str.count(charect) for charect in str }
print(word_count)





