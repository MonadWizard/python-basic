import re

mail = input('Enter mail: ')
addressToVerify = mail
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
print(match)

if match == None:
	print('Bad Syntax')