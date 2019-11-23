import os


pth = "D:\\code\\python\\basic\\coreFundamental\\Directory\\inpt"


if(os.path.isdir(pth)):
    print("Your needed directory is exist \n",os.getcwd())

else:    
    os.mkdir(pth)
    print(os.getcwd(),"\n change to \n",os.chdir(pth),os.getcwd())



  

while 1:
    inpt = input("enter file name with extention : ")
    inp = "\\"+inpt
    sub = pth+inp
    
    print('give file name or type q to exit')
    
    if(os.path.exists(sub)):
        print("Your needed file is exist \n",os.getcwd())
    
    
    elif inpt == 'q':
        break

    

    else:    
        os.mkdir(sub)
        print(sub , "\t file created")




print("print all directory inside of this path :", os.listdir(pth))




"""
print(os.path.isdir("D:\\X\\task"))
print(os.path.exists("D:\\X\\task\\dataset.txt"))
 
"""








"""
while 1:
    name = input("give: ")
    if name == 'q':break

"""