import string

for letter in string.ascii_lowercase:
    print(letter)

name = "rakib"
length = len(name)
print(length)
i = 0

nameL = list(name)
print(nameL[0],nameL[-1])

for n in range(-1,(-length-1),-1):
    print(name[i], "\t",name[n])
    print(name[i]+name[n])  #Concatination Operator(+)
    print(5*name[i])   # Replication Operator (*)
    i += 1
    print("\n")

print("___________________________________________________________")

"""Python String Membership Operators :   in      ,    not in """
str1 = "hellow Python world"
str2 = 'python'
str3 = "hPw"
print(str3 in str1)
print(str2 in str1)
print("""
""")

print("___________________________________________________________")

"""Python Relational Operators:  (<,><=,>=,==,!=,<>)  """
print(name == str1)
print ("Rakib">="rakib")
#print("Z" <> "z")  #py 3 not support <>  use !=
print("Z" != "z")
print("""
""")

print("______________________________________________________")

"""Python String Slice Notation: """
print("name[0:4] : ",name[0:4])
print("name[0:2] : " ,name[0:2])
print("name[2:4] : " ,name[2:4])
print("name[:4] : " ,name[:4])
print("name[3:] : " ,name[3:])
print("name[:5]+name[5:] : " ,name[:5]+name[5:])
print("name[:5]+name[3:] : " ,name[:5]+name[3:])
print("name[:3]+name[5:] : " ,name[:3]+name[5:])