
# use of infinity loop
is_programmer = False
while not is_programmer:
    print('learn programming....')
    user_is_programmer = input(f'Are you a programmer yet ?\n type only yes or no :')
    is_programmer = user_is_programmer == 'yes'
    
    

# general loop
i = 0
while i < 10:
    print(f'item is come to : {i}')
    i += 1
    

# another example of while with temperature
temperature = float(input(f'type any temperature between 10 to 20 : '))

while temperature < 23:
    print('increse heating.........')
    temperature += 1
print("now it's room temperature 22cc ......." )


    