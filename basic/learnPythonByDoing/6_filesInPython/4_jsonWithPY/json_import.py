"""
#json start and end with { }. and total inside of { } is caalled an object in js
#it's use nly "" not ''
#it's execute only string then need to convert python dictionary
# some programme ignor starting header { }
"""

import json
# 1st read contain friends_json.txt
file = open('friends_json.txt', 'r')

# load contain
file_contents = json.load(file) # now file_contents is a dictionary

# close file
file.close()

# print any index of dectionary which come to json
print(file_contents['friends'][1])
    


############create new json file and insert data
cars = [
        {'make': 'Ford', 'model': 'Fiesta'},
        {'make': 'Ford', 'model': 'Focus'}
        ]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()






############load json string to a dictionary
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])















