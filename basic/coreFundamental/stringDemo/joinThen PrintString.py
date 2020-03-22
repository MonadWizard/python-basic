s1 = str(input('Enter 1st string.'))
s2 = str(input('now give another string,'))

print('''
''')

print('length of first string',len(s1))
print('length of second string',len(s2))

print('''
''')

sf = (s1 +' ' + s2)
print ('after joining two string we found :', sf)
print('length of final string', len(sf))

print('now see after tokenization')
token = sf.split(' ')
print(token)
for a in token:
    print (a)


