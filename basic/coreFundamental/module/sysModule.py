import sys  # import system module

sys.stderr.write('this is stderr text\n') #stderr use for define error. it's same as stdout. 
sys.stderr.flush()  #>>>>???????????????????????
sys.stdout.write('This is stdout text\n')

print(sys.argv)

#print(sys.builtin_module_names,"\n") # to see build in module on python
print(sys.builtin_module_names[4])

#print("\n",sys.modules,"\n") # see every single module with path

#print(sys.modules.keys(),"\n") # see every single module

print(sys.platform)

print(sys.getwindowsversion())




