"""
Common Exceptions
ZeroDivisionError: Occurs when a number is divided by zero.
NameError: It occurs when a name is not found. It may be local or global.
IndentationError: If incorrect indentation is given.
IOError: It occurs when Input Output operation fails.
EOFError: It occurs when end of the file is reached and yet operations are being performed.
ect.......
"""

"""
Syntax:

try:  
    malicious code  
except Exception1:  
    execute code  
except Exception2:  
    execute code  
....  
....  
except ExceptionN:  
    execute code  
else:  
    In case of no exception, execute the else block code.  
"""

try:
    a = 10 / 0
    print(a)
except ArithmeticError:
    print("face exception")
    print("""
    """)
else:
    print("Welcome")

"""
Except statement can also be used without specifying Exception.
Syntax:

try:  
        code  
    except:  
        code to be executed in case exception occurs.  
    else:  
        code to be executed in case exception does not occur.   
"""

try:
    a = 10 / 0
except:
    print("Arithmetic Exception")
    print("""
    """)
else:
    print("Successfully Done")

"""
Finally Block:
In case if there is any code which the user want to be executed, 
whether exception occurs or not then that code can be placed inside the finally block.
Finally block will always be executed irrespective of the exception.

Syntax:
try:  
    Code  
finally:   
    code which is must to be executed. 
"""

try:
    a = 10 / 0
    print("Exception occurred")
except:
    print("Arithmetic Exception")
finally:
    print("Code to be executed")
    print("""
    """)
# In the above example finally block is executed. Since exception is not handled therefore exception occurred and execution is stopped.


"""
Raise an Exception:
You can explicitly throw an exception in Python using ?raise? statement. raise will cause an exception to occur and thus execution control will stop in case it is not handled.

Syntax:
raise Exception_class,<value>  
"""
try:
    a = 10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occurred")
    print(e)
    print("""
    """)

"""
we learn: how to "Raise buildin exception",   how to "raise user define exception",  how to use "finally" key word
"""

######## Raise buildin exception :
try:                                   #all exception have a generic class named "Exception"
    raise Exception("generic class define")   #not appropeat but usefull
    raise MemoryError("memory error")  # 1st give "raise" then "exception_class_name"(than give messageInParanteses)"
#    raise Exception("generic class define")  # allow first declaration on "raise"
except MemoryError as e:
    print(e)
    print("""
    """)
except Exception as ex:
    print(ex)
    print("""
    """)


"""
exception on python is acctually the instance of classes. So define a user define exception you need to define a class
"""





"""
Explanation:
i)To raise an exception, raise statement is used. It is followed by exception class name.
ii)Exception can be provided with a value that can be given in the parenthesis. (here, Hello)
iii)To access the value "as" keyword is used. "e" is used as a reference variable which stores the value of the exception.
"""




######## use "finally" keyword to handle exception

def process_file():
    try:
        f = open("D:\\code\\pyCham\\basic\\exceptionHandelingDmo\\demo.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside exception")
    finally:
        print("Clearing up file")  #face error cause I don't define ArithmaticErrpr in exception, but it complete finally block however it find exception and code crush
        f.close()
        print(".............................................")
        print("""
        """)

#process_file()     #process_file() method can't work without diclaration



