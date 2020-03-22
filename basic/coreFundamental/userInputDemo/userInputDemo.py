

x = input('what is your name ? ')
y = int(input('give Intrger'))

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





