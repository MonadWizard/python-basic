# Ask the user for a list of 3 friends.
# For each friend, we'll tell the user whether they are nearby.
# For each nearby friend, we'll save their name to 'nearby_friends.txt'


## take user input 3 friends name
friends = input('Enter three friend name, separate by commas(NO SPACE PLZ....) : ').split(',')
#['1stName', '2ndName', '3rdName'] splite and make indivusial Name


## now just read people.txt file, we write to nearbyFriend.txt file
people = open('people.txt', 'r' )
# readline as list with giving \n.['1stName\n', '2ndName\n', '3rdName\n'] so we need to remove \n to compare
#so we need set comprehention line.strip(), which can reduse \n,\t, or and space start to end
##people_nearby = people.readlines() # take \n 
people_nearby = [line.strip() for line in people.readlines()]


people.close()


#now find people whoes are friend and whoes are nearby. for that 1st we make a set

## now create 2 sets
friends_set = set(friends)
people_nearby_set = set(people_nearby)

## for execute match, we intersect  2 sets
friends_nearby_set = friends_set.intersection(people_nearby_set)

##open nearbyFriend.txt and write  
nearby_friends_file = open('nearbyFriend.txt', 'w')

## itterup friends and prient and also save to nearbyFriend.txt
for friends in friends_nearby_set:
    print(f'{friends} is nearby ! meet up with them.')
    nearby_friends_file.write(f'{friends}\n')
    
nearby_friends_file.close()




























