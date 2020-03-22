friends = [
        {'name': 'Rolf', 'location': 'washington, D.C.'},{'name': 'Anna', 'location': 'San Francisco'},
        {'name': 'Charlie', 'location': 'San Francisco'},{'name': 'Jose', 'location': 'San Francisco'}
        ]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]      # calculate which friend are in that location

# any() function returns true if any of them are true
# all() function returns true if all of them are true


if len(friends_nearby) > 0:
    print('you are not alone..!')

if any(friends_nearby):      # same as len # true if there's at least one; or false if empty
    print('any of you are not alone..!')


if all(friends_nearby):      # same as len # true if there's all is more than zero; or false if empty,or if any zero       
    print('all of you are not alone..!')
    
print(any([0, 1, 2, 3, 4, 5]))
print(any([1, 2, 3, 4, 5]))

print(all([0, 1, 2, 3, 4, 5]))
print(all([1, 2, 3, 4, 5]))



