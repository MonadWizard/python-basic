
# use break statement
cars = ['ok','ok','ok','faulty','ok','ok']
for car in cars:
    if car == 'faulty':
        print(f'stop production cars')
        break
    print(f'this is a {car} car.')
    
print("""
      """)

    
# use continue statement    
for car in cars:
    if car == 'faulty':
        print(f'stop production cars')
        continue # it skip present loop_operation after continue keyword then work next loop chacking 
    print(f'this is a {car} car')    #
    
print("""
      """)    
    
# print even odd or number
for num in range (2,10):
    if num % 2 == 0:
        print(f'Found even number, {num}')
        continue
#    print(f"FOUND A NUMBER {num}")


print("""
      """)

# other way to found prime number

for n in range(2,10): # [2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(2, n):  #[],[2],[2,3],[2,3,4],[2,3,4,5],[2,3,4,5,6],[2,3,4,5,6,7],[2,3,4,5,6,7,8]
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
        else:
            print(f'{n} is a prime number')
                