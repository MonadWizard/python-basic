"""
Attribute of file :
Name      Mode      closed

"""

obj = open("abcd.txt", "w")
print  (obj.name)
print  (obj.mode)
print  (obj.closed)





"""
A File can be opened in two modes:  (1) Text Mode      (2) Binary Mode

R	It opens in Reading mode. It is default mode of File. Pointer is at beginning of the file.
rb	It opens in Reading mode for binary format. It is the default mode. Pointer is at beginning of file.
r+	Opens file for reading and writing. Pointer is at beginning of file.
rb+	Opens file for reading and writing in binary format. Pointer is at beginning of file.
W	Opens file in Writing mode. If file already exists, then overwrite the file else create a new file.
wb	Opens file in Writing mode in binary format. If file already exists, then overwrite the file else create a new file.
w+	Opens file for reading and writing. If file already exists, then overwrite the file else create a new file.
wb+	Opens file for reading and writing in binary format. If file already exists, then overwrite the file else create a new file.
a	Opens file in Appending mode. If file already exists, then append the data at the end of existing file, else create a new file.
ab	Opens file in Appending mode in binary format. If file already exists, then append the data at the end of existing file, else create a new file.
a+	Opens file in reading and appending mode. If file already exists, then append the data at the end of existing file, else create a new file.
ab+	Opens file in reading and appending mode in binary format. If file already exists, then append the data at the end of existing file, else create a new file.

"""





"""
There are many methods related to File Handling. They are given in the following table:
There is a module "os" defined in Python that provides various functions which are used to perform various operations on Files.
 To use these functions 'os' needs to be imported.
 
 
rename()	It is used to rename a file. It takes two arguments, existing_file_name and new_file_name.
remove()	It is used to delete a file. It takes one argument. Pass the name of the file which is to be deleted as the argument of method.
mkdir()	    It is used to create a directory. A directory contains the files. It takes one argument which is the name of the directory.
chdir()	    It is used to change the current working directory. It takes one argument which is the name of the directory.
getcwd()	It gives the current working directory.
rmdir()	    It is used to delete a directory. It takes one argument which is the name of the directory.
tell()	    It is used to get the exact position in the file.

"""





"""
                                        rename():
Syntex : os.rename(existing_file_name, new_file_name)
"""
import os
#os.rename('pqr.txt','mno.txt')      #rename pqrs to mno




"""
                                          remove():
Syntax:    os.remove(file_name)  
"""
#os.remove('mno.txt')               #remove mno file






"""
                                            mkdir() : 
Syntax:   os.mkdir("file_name")
"""
#os.mkdir("new")        #make a folder name new





"""
                                             chdir():
Syntax:   os.chdir("file_name")
"""
#os.chdir("new")







"""
                                             getcwd()
Syntax:  os.getcwd()
"""
print (os.getcwd())








"""
                                             rmdir()
Syntax:   os.rmdir("directory_name)
"""
#os.rmdir("new")

