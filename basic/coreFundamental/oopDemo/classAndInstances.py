class Employee:
    num_of_emps = 0   # class variable
    raise_amount = 1.04  # class variable
    
    def __init__(self,first,last,pay):
        self.firstN = first
        self.lastN = last
        self.pay = pay
        self.email = first+ "." + last+ "@company.com"
        
        Employee.num_of_emps += 1
        
    def fullName(self):
        return '{} {}'.format(self.firstN, self.pay)
        
        
#   regular method pass automaticly self parameter
#   class method create by @classmethod then define method, class method pass automaticaly cls parameter
#   static method create by @staticmethod then define method, static method nothing pass automaticly
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
        
      
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


        
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


# from a string collect data using @classmethod
emp_str_1 = 'rakib-hasan-50000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)




# found is the day is woorking day using @staticmethod
import datetime
my_date = datetime.date(2019,9,11)

print(Employee.is_workday(my_date))







# now see number ofemploye
print(Employee.num_of_emps)

        
# define parameter which return by variable in __init__()
emp1 = Employee("Rakib", "Hasan", 9000)
emp2 = Employee("Rasid", "Hasan", 6000)

# now see number ofemploye
print(Employee.num_of_emps)


print(emp1)  # print emp1 location of memory

print(emp2.email)

print('{} {}'.format(emp1.firstN, emp2.lastN))

print(emp1.fullName())


# class variable are same for all variable
print(Employee.raise_amount) 
print(emp1.raise_amount)
print(emp2.raise_amount)

# give dictionary of emp1 value with key as __init__() parameter initial variable
print(emp1.__dict__)
# now diclar raise_amount to emp1
emp1.raise_amount = 1.05
# now we see emp1 have raise_amount key
print(emp1.__dict__)
















# for import file from another directory every directory need __init__.py file
# than from directory.file import ClassName
