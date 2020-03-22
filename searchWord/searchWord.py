"""
First Things First: Reading Data from a Text File.
In Python, reading a text file can be accomplished with the built-in open() function.



in_file = open("the-file-name.txt", "rt") # open file lorem.txt for reading text data
contents = in_file.read()         # read the entire file into a string variable
in_file.close()                   # close the file
print(contents)  		          # print contents



lines = [] #Declare an empty list named "lines"
with open ('t.txt', 'rt') as in_file:  #Open file lorem.txt for reading of text data.
    for line in in_file: #For each line of text store in a string variable named "line", and
        lines.append(line)  #add that line to our list of lines.
        print(line)        #print the list object.
        spl = line.split(' ')
#        print(spl)
        
"""

def wordcount(filename, listwords):
    try:
        file = open(filename, "r")
        read = file.readlines()
        file.close()
        for word in listwords:
            lower = word.lower()
            count = 0
            for sentance in read:
                line = sentance.split()
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("!@#$%^&*()_+-=")
                    if lower == line2:
                        count += 1
            print (lower, ":", count)
    except FileExistsError:
        print("This file is not there ")
        
wordcount("t.txt", ["syjvj"])
        

        
        













