class SimpleClass():
    
    def __init__(self, name):
        print("Hello "+name)
        
    def yell(self):
        print("Yelling")
        
s = "world"
x = SimpleClass("Rasid")

x.yell()


# Extend class
class ExtendedClass(SimpleClass):
    
    def __init__(self):
        #use Simpleclass __init__()
        super().__init__("Rakib")
        print("Extend..!")
    
y = ExtendedClass()

y.yell()


