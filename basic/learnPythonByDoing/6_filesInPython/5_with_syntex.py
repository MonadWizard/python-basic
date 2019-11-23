with open('demo.txt', 'r') as my_file:
    file_content = my_file.read()


print(file_content)

user_data = input('type what you want to type: ')

with open('demo.txt', 'w') as my_file_writing:    
    my_file_writing.write(user_data)

