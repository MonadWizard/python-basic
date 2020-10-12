

x = input('what is your name ? ')
y = int(input('give Intrger'))

x , y , z = input('''inter your name , your age,your sex, using * \n
                  ''' ).split('*')
                  
x , y ,z = "tuhin", "25", "male"



              
y = float(y)
print(type(y))




print("hellow" , x)
print("hellow2" , y)
print(type(x), type(y))

name,age = input("Enter your name and age seperated\
                 by , \n").split(",")

print(name, '\n', age)

# print name in reverse holder
a = 'Rakib'
print([(lambda x: x)(x) for x in a[-1::-1]])
print(a[-1::-1])
print([a[-1::-1]])





