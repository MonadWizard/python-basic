class Garage2:
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        print('This method is a work in progress.')
    
ford = Garage2()
ford.add_car('Fiesta1')
print(len(ford))
    
# in upper code len take 0 but it's not 0 so we face an error. now raise it
print("""
      """)

class Cars:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f'<Car {self.make}{self.model}>'
    
    
class Garage:
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car): 
        if not isinstance(car, Cars): # isinstance is a buildin function to diclar any parameter which are not on parameter
            raise TypeError(f'Tride to add a `{car.__class__.__name__}`to the garage, but you can only add `car` object.')
        self.cars.append(car)    
#        raise NotImplementedError("we can't add cars to the garage yet.") # now we can see where we face error
        
        
ford = Garage()
car = Cars('fiesta', 'ford')
ford.add_car(car)
print(len(ford))
    
    
    
    
    