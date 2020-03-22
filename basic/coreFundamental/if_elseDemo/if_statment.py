indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "rissoto"]

dish = input("Enter dish name you want : ")

if dish in indian:
    print("we found , you need indian dish")
elif dish in chinese:
    print("we found , you need chinese dish")
elif dish in italian:
    print("We found , you need italian dish")

else:
    print("sorry.....may be your searched dish is out of our stoke ")







usa = ["atlanta","new york","chicago","baltimore"]
uk = ["london","bristol","cambridge"]
india = ["mumbai","delhi","banglore"]

inputt = input("enter city name you want :")

if inputt in usa:
    print("this city in usa")
elif inputt in uk:
    print("city in uk")
elif inputt in india:
    print("city in india")
else:
    print("sorry ...not found")








input2 = input("enter first city name : ")
input3 = input("enter second city name : ")

if input2 in usa and input3 in usa:
    print ("both cities are in usa")
elif input2 in uk and input3 in uk:
    print("both cities are in UK")
elif input2 in india and input3 in india:
    print("both are in india")
else:
    print("sorry those cities are not in sane country")












print("here a result to see even or odd your enter number is.")
var = input("Enter a number")
var = int(var)
if var % 2 == 0:
    print("number is even and number is : ", var)
else:
    print("number is odd and number is : ", var)
