inp = int(input("input number of row : "))

for i in range(1, inp + 1):
    for j in range(1, i + 1):
        print("*", end=" #")
    print()  #new line

""" we arrange row and column wise so we need two loop one for row and another for column.
we also need another function name range .
"""
# range(0,11)         #it print 0 to 10    cause o is included and 11 is excluded
print('''


''')
for i in range(0, 11):
    print(i)

# we need to learn using interprater by type   help(print)
print("Rakib")
print("Hasan")  # use ; then give another print so it by default end create new line before print next print operation
print("Rakib", end=" ");
print(
    "Hasan")  # we decler end=" " , so now after 1st print operation it don't create defaultly new line,it added to end our initial value which is now space
