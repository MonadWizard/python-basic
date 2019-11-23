#name = input('Enter your name')
#print(f"Hello , {name} !")

def greet():
    name = input('Enter your name : ')
    print(f'hello {name} ..!')
    
greet()


# execure prime number using function
def check_if_prime(number):     #number is called a parameter
    for x in range(2, number):
        if number % x == 0:
            print(f'{number} equals {x} * {number//x}')
            break
    else:
        # loop fell through without finding a factor
        print(f'{number} is a prime number')
            
def check_primes(limit):
    for n in range(2, limit):
        check_if_prime(n)  # n is called an argument
            
check_primes(100)
            


