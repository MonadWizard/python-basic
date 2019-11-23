#   open(filename,mode)        there are 3 mod . read mod , write mod , append mod

tx_file = open("tet.txt",'w')    # use w to write and if no exist it creat txt file as it name
tx_file.write("hello people to ")      # write function to write a line
tx_file.write("rakib")
tx_file.close()                     #we need to close function unless it cann't finish process

tx_file = open("tet.txt",'a')    #use a to append or write text at end of previous text
tx_file.write("\n 2nd time")
tx_file.close()

tx_file = open("tet.txt",'r')    #use r to read text file
print(tx_file.read())
tx_file.close()





