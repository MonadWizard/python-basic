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

# iterable is an object which have  __iter__(self) 

    def __iter__(self):
        return FirstHundredGenerator()
    
print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)   


# __len__(self), __getitem__(self, i)  both are iterable
class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
for car in AnotherIterable():
    print(car)

# now see list and generator comprehention
my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])

print(my_numbers)


print(my_numbers_gen)

print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))

