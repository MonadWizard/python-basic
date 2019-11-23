file = open('csvdata.txt', 'r')
lines = file.readlines()
file.close()

## [value :] called lest sliceing
lines = [line.strip() for line in lines[1:]] #make comprehention for .readlines().it's execute from row index 1 and total column, it miss index 0 list

for line in lines:
    persion_data = line.split(',')
    name = persion_data[0]
    age = persion_data[1]
#    university = persion_data[2].title()
    university = persion_data[2]
#    degree = persion_data[3].capitalize()    
    degree = persion_data[3]
    
    print(f'{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}.')

sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)

"""
## write on csv  
write_sample_csv_value = open('csvdata.txt', 'w')

write_sample_csv_value.write(f'{sample_csv_value}\n') 
write_sample_csv_value.close()
"""

#task add after 
"""
name,age,university,degree
Rakib,24,mit,computer scince
Rasid,16,high school,scince
Akfa,45,house,wife
Bakul,57,house,husband
"""

