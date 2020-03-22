from oopDemo.classAndInstances import Employee

class Developer(Employee):
    raise_amt = 1.10
    
    
    def __init__(self,first,last,pay,prog_long):
        super().__init__(first,last,pay)
        self.prog_lang = prog_long
        
    



dev1 = Developer("Rakib", "Hasan", 9000, "Python")
dev2 = Developer("Rasid", "Hassan", 7000,"None")



print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)




















