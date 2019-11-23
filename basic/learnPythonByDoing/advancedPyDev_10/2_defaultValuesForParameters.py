accounts ={
        'checking': 1958.00,
        'savings': 3695.50
        }

#    Function to update the balance of an account and return the  new balance.
def add_balance(amount: float, name: str) -> float:  #type Hinting
    accounts[name] += amount
    return accounts[name]


print(accounts['savings'])
print(accounts['checking'])

print("""
      """)

add_balance(500.00, 'savings')
add_balance(1000.5, 'checking')

print(accounts['savings'])
print(accounts['checking'])



#default value must declar after non-default value
def add_balance(amount: float, name: str = 'savings') -> float:  #type Hinting
    accounts[name] += amount
    return accounts[name]

add_balance(500.00)

print('saving is key and value is', accounts['savings'])

""" #error happend
#default value must declar after non-default value
def add_balance( name: str = 'savings', amount: float) -> float:  #type Hinting
    accounts[name] += amount
    return accounts[name]

add_balance(500.00)

print('saving is key and value is', accounts['savings'])

"""
