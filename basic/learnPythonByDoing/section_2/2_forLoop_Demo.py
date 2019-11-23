primes = [2,3,5,7,11]
for prime in primes:
    print(f'prime number of the list is : {prime}')
    

  
kid_age = (3,8,11)
for age in kid_age :
    number = kid_age.index(age) + 1
    print(f'my {number} number kid age is :{age}')
        
    
    
for i in range(20,30,3):
    print(i)
    
    
my_friends = {
        'f1' : 6,
        'f2' : 12,
        'f3' : 18,
        'f4' : 24
        }


for name in my_friends:
    print(f'I saw {name} total {my_friends[name]} days ago.')
 
print("""
      """)    
    
# in python3 you can use more variable using .items()   
for name, days in my_friends.items():
    print(f'I saw {name} total {days} days ago')


print("""
      """)
    
for n, d in my_friends.items():
    if n == 'f3':
        print(f'I know {n} as my friend.')

who_do_i_know = input(f"Enter friend name : ")
if who_do_i_know in my_friends:
    print(f"I also know {who_do_i_know} as my friend.")
else:
    print("sorry I don't know this person.")


# now see truple destructering
for t in[('a',1,'A'),('b',2,'B'),('c',3,'C')]:
    (s,n,b) = t
    print(s)
    print(n)
    print(b)
    print(t)







