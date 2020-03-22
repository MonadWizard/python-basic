""""
Dictionary allows you to store key , value pairs
Also known as Maps,Hashtables,Associate Arrays
"""

"""       Example using interpreter
>>> d = {"a":356551,"b":54654,"c":654}
>>> d
{'a': 356551, 'b': 54654, 'c': 654}
>>> d["a"]
356551
>>> d["e"]=436436                                         #add new value
>>> d
{'a': 356551, 'b': 54654, 'c': 654, 'e': 436436}
>>> del d["e"]                                             #del to delete 
>>> d
{'a': 356551, 'b': 54654, 'c': 654}
>>> for key in d:                                           #display total key and value serially
...     print("key:",key,"value:",d[key])
...
key: a value: 356551
key: b value: 54654
key: c value: 654
>>> for k,v in d.items():                                   #display total key and value serially (alternative)
...     print("key:",key,"value",v)
...
key: a value 356551
key: b value 54654
key: c value 654


>>> "b" in d
True                                                    #to find out any value in dictionary
>>> d
{'a': 356551, 'b': 54654, 'c': 654}
>>> "s" in d                                            #to find out any value in dictionary
False
>>>
>>>
>>> d.clear()                                           #to clean all element from dictionary 
>>> d
{}


"""

d = {"Bakul": 56, "Akfa": 40, "Rakib": 25, "Rasid": 17}
inp3 = int(input("type 1 for Add person data 2 for search name to see age "))

if inp3 == 1:
    inp = input("Enter person name : ")
    inp2 = int(input("Enter person age : "))
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
