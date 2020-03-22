for b, a in enumerate(range(1,10,2)):
    print("1 to 10 by {first}st deference is {difference:02.3f}".format( first= b , difference = a))


li = ["rakib","Rakib","raKib"]

def check(listt,tergate):
    for pos,name in enumerate(listt):
        if name == tergate :
            return pos
    return -1

print(check(li,'raKib'))




















