# general test:
"""
import time

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

"""

# work with thread
"""
import time
from threading import Thread


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


# below use thread and upside code is regulat
# thread use for redusing wait time.


thread1 = Thread(target = complex_calculation)      # define 1 function on thread
thread2 = Thread(target = ask_user)     # define another function on thread


thread1.start()     # start thread1
thread2.start()     #start thread2

# we have 3 thread 1 for run total code which is main thread
# now we wait main thread until finish those 2 threads

# .join() called mainfunction to wait until finish diclared thread 
thread1.join()
thread2.join()

print(f'two thread total time: {time.time() - start}')
"""




#we can also write our thread by importing ThreadPoolExecutor

import time
from concurrent.futures import ThreadPoolExecutor


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
print(f'Single Thread total time, {time.time() - (start)}')

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)
    
# if we don't use with statement then we need 
# pool.shutdown()

print(f'two thread total time: {time.time() - start}')
