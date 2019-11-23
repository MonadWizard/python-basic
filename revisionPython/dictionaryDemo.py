def basic():

    a = {'name':"Rakib", "address":"Rajshahi","Work":"Programming"}

    for data in a:
        print('Your {k} = {v}'.format(k=data, v=a[data]))

    print(sorted(a.items(), key = lambda b:b[0]))

    x = 'name' in a
    print(x)              

    del a['name']
    print(a)



    d = {"a":356551,"b":54654,"c":654}
    for k,v in d.items():                                   #display total key and value serially (alternative)
        print("key:",k,"value",v)

    x = d.clear()
    print(x)





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








"""
python function :
len(dictionary),    cmp(dictionary1,dictionary2),    str(dictionary)
python method :
keys(),    values(),    items(),    update(dictionary2),    clear(),    fromkeys(sequence,value1)/ fromkeys(sequence)
copy(),     get(key)
"""



def function_dic():
    data = {100: 'Ram', 101: 'Suraj', 102: 'Alok'}

    print(len(data))    # see length

    print(str(data))    # see dictionary
    print(data)

    print(data.keys(), '\n', data.values())    # see key OR value
    
    print(data.items())   #see separately in a list 

    dataN = {103: 'new'}
    data.update(dataN)    # update and add key&value from dataN to data
    print(data, '\n', dataN)
    
    dataN.clear()  # create {} dictionary
    print(dataN)


    seq = {'F_name', 'last name', 'age', 'extra'}    # key formating
    data_seq = data.fromkeys(seq)
    print(data_seq)
    data_seq =data.fromkeys(seq, 100)    # inseert a data to formate
    print(data_seq)

    print(dataN)
    print(data_seq)
    dataN = data_seq.copy()     # copy from data_seq to dataN
    print('\n',dataN)

    print(dataN.get(1000))   # check key if present then give value unless give None
    print(dataN.get('age'))







# give function  and see work
