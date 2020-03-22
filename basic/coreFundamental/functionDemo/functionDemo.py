def calculate_total(exp):  # we use def to diclat any function and inside the ()parameter we declar return value
    i = 0
    for item in exp:
        i = i + item
    return i


li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
li2 = [15165, 61651, 65161, 516, 5616, 61, 6, 161, 61, 61, 616, 16, 161648, 98, 49, 79, 79, 7]

li1_total = calculate_total(li1)
li2_total = calculate_total(li2)

print("total of  li1 total is : ", calculate_total(li1))
print("total of  li2 total is : ", calculate_total(li2))


# demo of working function
def sum(a, b):
    total = a + b
    return total


n = sum(5, 6)
print("Total : ", n)


# demo of working details function
def sum2(a, b=0):
    print("a : ", a)
    print("b : ", b)

    total = a + b
    print("total : ", total)
    # return total


# n = sum2(8, 5)
n = sum2(8)
print("Total : ", n)

var = 10


def funcl():
    global var
    var = var + 1
    print("gloobal var incress 1 in local file by using globl keyword : ", var)
    return


funcl()  # need to assign it
