import math

nu = int(input("please enter the number : "))
try:
    res = math.factorial(nu)
    print(res)                  #if we use negative value it face error

#we can assign the type  of exception as it is ValueError
except ValueError:
    print("cann't compute - value")
#or
except:
    print("can't compute negative : ")




