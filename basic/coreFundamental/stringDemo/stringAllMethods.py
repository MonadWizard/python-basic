"""
all string method
capitalize(),   count(string,begin,end),    endswith(suffix ,begin=0,end=n),    find(substring ,beginIndex, endIndex),
index(subsring, beginIndex, endIndex),    isalnum(),    isalpha(),  isdigit(),  islower(),  isupper(),  isspace(),  len(string),
lower(),    upper(),    startswith(str ,begin=0,end=n),      swapcase(),    lstrip(),   rstrip(),

"""


name = "Rakib Hasan Rakib"
name1 = "rakibhasanrakib"
name2 = "1rakib2hasan3Rakib"
num = "356354684"


print("######## count(stringDemo) : ")
subname = "a"
print(name.count(subname,4,16))
print(name.count(subname,1,26))
print(name.count(subname,4,166))
print(name.count(subname))
print("""
""")


print("######## find(stringDemo) : ")
subname2 = "hasan"
subname3 = "Hasan"
print(name.find(subname))  #give find 1st index
print(name.find(subname2)) # -1 represent nothing to find
print(name.find(subname3))
print(name.find(subname3,3,10))
print(name.find(subname3,6))
print("""
""")




#### This method returns True if characters in the stringDemo are alphanumeric
print("######## isalnum() : ")
print(name.isalnum())    #false
print(name1.isalnum())   #True
print(name2.isalnum())    #true
print(subname2.isalnum())    #true
print("""
""")


#####  It returns True when all the characters are alphabets
print("######## isalpha() : ")
print(name.isalpha())
print(name1.isalpha())
print(name2.isalpha())
print("""
""")




#### This method returns True if all the characters are digit
print("######## isdigit() : ")
print(name.isdigit())
print(name1.isdigit())
print(name.isdigit())
print(num.isdigit())
print("""
""")




#### This method returns True if the characters of a stringDemo are in lower case
print("######## islower() :")
a = "rakib hasan"
print(name.islower())
print(name1.islower())
print(a.islower())
print(num.islower())
print("""
""")



#### This method returns False if characters of a stringDemo are in Upper case
print("######## isupper() :")
b = "RAKIBHASAN"
c = "RAKIB HASAN"
print(name.isupper())
print(num.isupper())
print(b.isupper())
print(c.isupper())
print("""
""")




#### This method returns True if the characters of a stringDemo are whitespace
print("######### isspace()  : ")
space = " "
print(name.isspace())
print(name2.isspace())
print(num.isspace())
print(space.isspace())
print("""
""")




#### this meyhod return length of a stringDemo
print("######## len(stringDemo) : ")
print(len(num))
print(len(name))
print(len(name2))
print("""
""")



#### It converts all the characters of a stringDemo to Lower case.
print("######## lower() : ")
print(name.lower())
print(name1.lower())
print(num.lower())
print(a.lower())
print("""
""")



##### This method converts all the characters of a stringDemo to upper case.
print("######## upper() : ")
print(name.upper())
print(name1.upper())
print(num.upper())
print("""
""")




#### This method returns a Boolean value if the stringDemo starts with given str between begin and end.
print("######## startswith(stringDemo) : ")
print(name.startswith("rakib"))
print(name1.startswith("rakib"))
print(name2.startswith("rakib"))




#### It inverts case of all characters in a stringDemo.
print("######## swapcase() :")
print(name.swapcase())
print(name1.swapcase())
print(num.swapcase())
print("""
""")



#### It removes all leading whitespace of a stringDemo and can also be used to remove particular character from leading.
print("######## lstrip() : ")
hashT = "#########fuck"
print(name.lstrip("Rakib"))
print(name2.strip("1"))
print(hashT.strip("#"))





#### It removes all trailing whitespace of a stringDemo and can also be used to remove particular character from trailing.
print("######## rstrip() :")
string1 = "    Hello Python     "
print(string1.rstrip())
string2="@welcome to SSSIT!!!"
print(string2.rstrip('!'))




