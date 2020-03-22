from oopDemo.classAndInstances import Employee
from oopDemo.inheritance.developers import Developer

class Manager(Employee):
    
    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
        
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())



dev1 = Developer("Rakib", "Hasan", 9000, "Python")
dev2 = Developer("Rasid", "Hassan", 7000,"none")


mgr1 = Manager("rakib", "hasan", 10000, "python")

print(mgr1.email)



"""   Need to fix this problems     """

#mgr1.add_emp(dev2)
#mgr1.remove_emp(dev1)

#mgr1.print_emps()


































