import math
num = int(input("Enter input : "))
try:
    res = math.factorial(num)
    print(res)
except:
    print("yoou occer exception...")
finally:
    print("good bye.....!")