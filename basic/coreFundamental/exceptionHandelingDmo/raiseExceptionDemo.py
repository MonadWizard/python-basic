try:
    num = int(input("Enter a number : "))
    if num <=0:
        raise ValueError("this is not positive number")
except ValueError as error:
    print(error)


    