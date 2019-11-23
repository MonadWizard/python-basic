my_friend = {
        'f1' : 5,
        'f2' : 10,
        'f3' :30
        }

my_friends = {
        'f1' : {'last_seen' : 6,'2nd_last_seen' : 11},
        'f2' : {'name' : 'unknown'},
        'f3' : 6
        }

players = [
        {
                'name' : 'unknown1',
                'numbers' : (13,22,3,6,9)
                },
        {
                'name' : 'unknown2',
                'numbers' : (22,3,5,7,9)
                }
        ]


player_one = players[0]
player_two = players[1]

print("name of player one is " , player_one['name'],"\n number of goals is : ", player_one['numbers'],
      "\n sum of goal is : " , sum(player_one['numbers']))




