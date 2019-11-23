accounts ={
        'checking': 1958.00,
        'savings': 3695.50
        }

#    Function to update the balance of an account and return the  new balance.
def add_balance(amount: float, name: str) -> float:  #type Hinting
    accounts[name] += amount
    return accounts[name]


transactions = [
        (-180.67, 'checking'),
        (-220.00, 'checking'),
        (180.90, 'savings'),
        (-18.67, 'checking'),
        (-25.70, 'checking'),
        (-13.67, 'savings'),
        (-580.67, 'checking'),
        (-600.50, 'savings'),
        (600.50, 'checking'),
        ]


# add all transactions to accounts
for t in transactions:
#    add_balance(t[0], t[1]) # or
#    add_balance(amount=t[0], name=[1]) # or      
    add_balance(*t)  # each element of t have separate value   * means unpacking operator which can unpack argoment 
    







