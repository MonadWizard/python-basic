class FixFloat:
    def __init__(self, amount):
        self.amountt = amount
        
    def __repr__(self):
        return f'<FixFloat {self.amountt:.2f}'


    def from_sum(self, value1, value2):
        return FixFloat(value1 + value2)

    @staticmethod  # use for declar class.method or minimize self argoment
    def from_summ(value1, value2):
        return FixFloat(value1 + value2)
    
    @classmethod  # mxost usefull then static method
    def from_sumc(cls, value1, value2): # need to add 3 agr and 1st one use to call define class
        return cls(value1 + value2)


number = FixFloat(18.6746)
print(number)
new_number = number.from_sum(19.676, 0.789)
print(new_number)

new_number2 = FixFloat.from_summ(19.676, 0.789)  #using @staticmethod we dont need to create object
print(new_number2)


class Euro(FixFloat):
    def __init__(self, amount2):
        super().__init__(amount2)
        self.symbol = '€'
    
    
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amountt:.2f}>'
    
    
money = Euro(18.786)
print(money)

print(money.from_sum(16.788, 9.999))   
money2 = Euro.from_sumc(16.788, 9.999)
print(money2)    
    
    
    
    
    