import re
a = input("Input text: ")
b = a.split("//")
c = b[0].split()
print(" ".join(str(x) for x in c))