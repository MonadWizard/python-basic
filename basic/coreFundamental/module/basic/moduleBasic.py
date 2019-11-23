"""
Modules are used to categorize Pyhton code into smaller parts.
A module is simply a Python file, where classes, functions and variables are defined.
Grouping similar code into a single file makes it easy to access.
Thus module is simplify a python code where classes, variables and functions are defined.
"""

"""
ython provides the following advantages for using module:
1) Reusability: Module can be used in some other python code. Hence it provides the facility of code reusability.
2) Categorization: Similar type of attributes can be placed in one module.
"""

"""
"import" statement can be used to import a module.
Syntax:
import <file_name1, file_name2,...file_name(n)="">  
</file_name1,>  
"""



"""
NOTE: You can access any function which is inside a module by module name and function name separated by dot. 
It is also known as period. Whole notation is known as dot notation.
"""
import addition
addition.add(10,20)
addition.add(30,40)

import msg
msg.msg_method()
msg.display_method()
print("..........................................................")


"""
from..import statement is used to import particular attribute from a module. 
In case you do not want whole of the module to be imported then you can use from ?import statement.
Syntax:
from  <module_name> import <attribute1,attribute2,attribute3,...attributen>     
</attribute1,attribute2,attribute3,...attributen></module_name>  
"""
from msg import square,rectangle
square(10)
rectangle(2,5)
print(".................................................")


"""
You can import whole of the module using "from? import *"
Syntax:
        from <module_name> import *  
        </module_name>  
Using the above statement all the attributes defined in the module will be imported and hence you can access each attribute.
"""

from msg import *
square(10)
rectangle(2,5)
circle(5)
triangle(10,20)
print("...................................................")


"""
There are many built in modules in Python. Some of them are as follows:
math, random , threading , collections , os , mailbox , string , time , tkinter etc..
Each module has a number of built in functions which can be used to perform various functions.
Let?s have a look over each module:
1) math:
Using math module , you can use different built in mathematical functions.
ceil(n)	It returns the next integer number of the given number
sqrt(n)	It returns the Square root of the given number.
exp(n)	It returns the natural logarithm e raised to the given number
floor(n)	It returns the previous integer number of the given number.
log(n,baseto)	It returns the natural logarithm of the number.
pow(baseto, exp)	It returns baseto raised to the exp power.
sin(n)	It returns sine of the given radian.
cos(n)	It returns cosine of the given radian.
tan(n)	It returns tangent of the given radian.


"""
import math
a=4.6
print (math.ceil(a))
print (math.floor(a))
b=9
print (math.sqrt(b))
print (math.exp(3.0))
print (math.log(2.0))
print (math.pow(2.0,3.0))
print (math.sin(0))
print (math.cos(0))
print (math.tan(45))
print("..................................................")
print("""
""")

"""
he math module provides two constants for mathematical Operations:
Pi	Returns constant ? = 3.14159...
ceil(n)	Returns constant e= 2.71828...
"""
print (math.pi)
print (math.e)
print("..........................................................")
print("""
""")


"""
The random module is used to generate the random numbers. It provides the following two built in functions:
Function	Description
random()	It returns a random number between 0.0 and 1.0 where 1.0 is exclusive.
randint(x,y)	It returns a random number between x and y where both the numbers are inclusive.
"""
import random
print (random.random())
print (random.randint(2,8))
print("................................")
print("""
""")




"""
The primary use of __init__.py is to initialize Python packages. 
The easiest way to demonstrate this is to take a look at the structure of a standard Python module.

package/
    __init__.py
    file.py
    file2.py
    file3.py
    subpackage/
        __init__.py
        submodule1.py
        submodule2.py

As you can see in the structure above the inclusion of the __init__.py file in a directory indicates to the Python interpreter 
that the directory should be treated like a Python package

"""



"""
What goes in __init__.py?

__init__.py can be an empty file but it is often used to perform setup needed for the package(import things, load things into path, etc).

One common thing to do in your __init__.py is to import selected Classes, functions, etc into the package level 
so they can be convieniently imported from the package.

In our example above we can say that file.py has the Class File. So without anything in our __init__.py you would import with this syntax:

from package.file import File
However you can import File into your __init__.py to make it available at the package level:

# in your __init__.py
from file import File

# now import File from package
from package import File
Another thing to do is at the package level make subpackages/modules available with the __all__ variable. 
When the interpeter sees an __all__ variable defined in  an __init__.py it imports the modules listed in
 the __all__ variable when you do:

from package import *
__all__ is a list containing the names of modules that you want to be imported with import * 
so looking at our above example again if we wanted to import the submodules in subpackage 
the __all__ variable in subpackage/__init__.py would be:

__all__ = ['submodule1', 'submodule2']
With the __all__ variable populated like that, when you perform

from subpackage import *
it would import submodule1 and submodule2.

As you can see __init__.py can be very useful besides its primary function of indicating that a directory is a module

"""














