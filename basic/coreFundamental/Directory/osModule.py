import os

curDir = os.getcwd() # getcwd use to get current directory 
print(curDir) # print current working directory 

os.mkdir('newDir') # mkdir use to make a new directory by name of it's parameter

import time 

time.sleep(2) # sleep use to wait by given seconds on it's parameter

os.rename('newDir','newDir2')  # rename method have two parameter. 1st is old_NAME 2nd is new_NAME.
time.sleep(2)

os.rmdir('newDir2') # rmdir use to remove directory by passing directory name as it's parameter.

