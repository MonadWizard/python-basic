"""
import time
from multiprocessing import Process



def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user,{time.time() - start}')
    

def complex_calculation():
    start = time.time()
    print('Started calculating.....')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')
    
    
start = time.time()
ask_user()
complex_calculation()
print(f'complex_calculation, {time.time() - (start)}')


# now work with process
process = Process(target = complex_calculation)
#process2 = Process(target = ask_user)      # face error cause process can't share space or take user input easily
process2 = Process(target = complex_calculation)

process.start()
process2.start()

start = time.time()

ask_user()

process.join()
process2.join()



print(f'two process total time: {time.time() - start}')
"""




# we can also work with ProcessPoolExecutor

import time
from concurrent.futures import ProcessPoolExecutor



def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user,{time.time() - start}')
    

def complex_calculation():
    start = time.time()
    print('Started calculating.....')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')
    
    
start = time.time()
ask_user()
complex_calculation()
print(f'complex_calculation, {time.time() - (start)}')


# now work with processPoolExecutor

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    
print(f'two process total time: {time.time() - start}')







