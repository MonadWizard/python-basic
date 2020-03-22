class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
        
    def __next__(self):    #next dunder can provide any object as  next(my_object)  as generator
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
            
my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))
print(my_gen.__next__())
print(my_gen.__next__())


"""
# we cann't declar __next__ on loop
for i in my_gen:
    print(i)

"""










