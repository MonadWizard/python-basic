my_file = open('demo.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_data = input('type what you want : ')

my_file_writing = open('demo.txt', 'w')
my_file_writing.write(user_data)

my_file_writing.close()

