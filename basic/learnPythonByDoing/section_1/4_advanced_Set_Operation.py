set_one = {1, 2,7, 3, 4, 5,55}
set_two = {1, 3, 5, 7, 9, 11}

# we work with union of sets, intersection of sets, difference between sets

#___intersection of sets is the element of two sets are matching 
print(set_one.intersection(set_two))
print(set_one & set_two)

print("""
      """)
#___union of two sets is work with mathch and the difference of elements in two sets are take together without duplicate
print(set_one.union(set_two))
print(set_one | set_two)

print("""
      """)
#___difference between two sets is, just print unmatch element of 1st set
print(set_one.difference(set_two))
print(set_one - set_two)

print("""
      """)



