
s = "where's waldo?"
s.find("waldo")

# if not found it return -1
s.find("rakib")

# we can found in position 
s.find("waldo, 0, 6")



# string.index(substring, start, end)  start end optional
s = "where's waldo?"
s.index("waldo")

# index need to handel exception if sub-string not found.
try:
    s.index("Rakib")
except ValueError:
    print("Not Found")

# string.count(substring) use to find how many time substring is in string

s1 = "how fruits is fruits are fruits here fruits now !"
s1.count("fruits")

# we can give limit
s1.count("fruits", 0, 10)

# replace substring to another substring
# string.replace(old,new,count)         count optional
s1.replace("fruits", "Rakib")

# we can define how many replace happend
s1.replace("fruits", "Rakib", 2)




