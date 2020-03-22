d = {"a":356551,"b":54654,"c":654}
print(d)

# add new value 
d["e"] = 414
print(d)

# delete a value
del d["a"]
print(d)

# display total key and value serially
for k in d:
    print("key:", k, "    value:",d[k])

print("\n\n\n")

#or
for k,v in d.items():
    print("key:",k,"    value",v)


# find out any value in dictionary
print("b" in d)
print("s" in d)

# to clean a dictionary
d.clear()
print(d)





d = {"Bakul": 56, "Akfa": 40, "Rakib": 25, "Rasid": 17}
inp3 = int(input("type 1 for Add person data 2 for search name to see age "))

if inp3 == 1:
    inp = input("Enter person name : ")
    inp2 = int(input("Enter person age"))
    d[inp] = inp2

    print('''
    ''')
    inp4 = input("Enter search person name to see his age : ")
    print(inp4, "'s age is : ", d[inp4])

elif inp3 == 2:
    inp4 = input("Enter search person  name to see his age : ")
    print(inp4, "'s age is : ", d[inp4])
else:
    print("please enter between 1 or 2 ")



