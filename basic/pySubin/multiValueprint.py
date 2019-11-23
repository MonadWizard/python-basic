def fnc(x, y, z = None):
	print ('x , y, z :', x , y , z)

	x = x * x
	y = y * y
	if z is None:
		z = []

	return x, y, z


#pack to taple
print 'pack to taple'
print fnc(10,20,30)	

#unpack to taple
print 'unpack to taple'
x, y, z = fnc(10,20)
print x
print y
print z