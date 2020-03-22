# simple while loop

def hundred_numbersSimple():
    num = []
    i = 0
    while i < 100:
        num.append(i)
        i += 1
    return num
        
g = hundred_numbersSimple()
print("1st_S :", g)



# generator works by yield

def hundred_numbersGenerator():
    i = 0
    while i < 100:
        yield i
        i += 1
        
g = hundred_numbersGenerator()
print("1st_G :",next(g))
print("2nd_G :",next(g))
print("3rd_G :",next(g))
print("4th_G :",next(g))

print("List_G :",list(g))
