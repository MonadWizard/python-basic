"""   r for read    w for write    r+ for read & write both
w+ for read & write both , if don't exist create one , if exist than over write    a for open on append mood  """





'''  write an script to txt file  '''
f = open("D:\\code\\pytotxt\\funny.txt", "a")
inp = input("Enter text here ")
f.write("\n")
f.writelines(inp)
f.close()

'''  read the scrept of txt    '''
f = open("D:\\code\\pytotxt\\funny.txt", "r")
for line in f:
    print(line)
# print(f.read())
f.close()

'''   count number of word on txt   '''
f = open("D:\\code\\pytotxt\\funny.txt", "r")
for line in f:
    tokens = line.split(' ')
    print(str(tokens))
    print(len(tokens))
f.close()


'''   save as new    '''
f = open("D:\\code\\pytotxt\\funny.txt", "r")
f_out = open("D:\\code\\pytotxt\\funny2.txt", "w")
for line in f:
    tokens = line.split(' ')
    f_out.write(line + "\n" + "wordcount : " + str(len(tokens)))
f.close()
f_out.close()




'''   automatic close file  with statement '''
with open("D:\\code\\pytotxt\\funny.txt", "r") as f:
    print(f.read())

print(f.closed)