"""
Python provides the facility of working on Files. A File is an external storage on hard disk from where data can be stored and retrieved.
"""



"""
To open a File, Python built in function open() is used. It returns an object of File which is used with other functions. 
Having opened the file now you can perform read, write, etc. operations on the File.
Syntex : obj=open(filename , mode , buffer)   
                    filename:It is the name of the file which you want to access.
                    mode:    It specifies the mode in which File is to be opened.There are many types of mode.
                             Mode depends the operation to be performed on File. Default access mode is read.
"""


"""
Closing a File:Once you are finished with the operations on File at the end you need to close the file.
It is done by the close() method. close() method is used to close a File.
Syntex :  fileobject.close()   
"""


"""
Writing to a File:write() method is used to write a string into a file.
Syntex : fileobject.write(string str)  
"""


"""
Reading from a File:read() method is used to read data from the File.
Syntex : fileobject.read(value)
                    here, value is the number of bytes to be read. In case, no value is given it reads till end of file is reached.
"""





obj=open("abcd.txt","w")
obj.write("Welcome to the world of Python")
obj.close()
obj1=open("abcd.txt","r")
s=obj1.read()
print (s)  
obj1.close()
obj2=open("abcd.txt","r")
s1=obj2.read(20)
print (s1)
obj2.close()






















