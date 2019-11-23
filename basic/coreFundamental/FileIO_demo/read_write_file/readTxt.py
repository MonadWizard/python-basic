# 'r' define it's read type
readMe = open('tet.txt','r').read()  #.read() function just display total txt file
print("read : ",readMe)

readMe2 = open('tet.txt','r').readline(5) #.readline(5) display first 5 character
print("readline(5)",readMe2)

readMe4 = open('tet.txt','r').readline() #.readline() display first line
print("readline()",readMe4)



readMe3 = open('tet.txt','r').readlines()   #make all line as array index's value
print("readlines",readMe3)

