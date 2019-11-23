friends = ['FRIEND','UNKNOWN','FRIEND2','FRIEND3','LEGEND']

friends_lower = map(lambda x: x.lower(), friends)
friends_lower2 = [friend.lower() for friend in friends]
friends_lower3 = (friend.lower() for friend in friends)

print(next(friends_lower3))
print(list(friends_lower3))
print("\n\n")
#print(next(friends_lower2))        # can't assign
print(list(friends_lower2))
print("\n\n")
print(next(friends_lower))
print(list(friends_lower))



"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        @classmethod
        def from_dict(cls, data):
            return cls(data['username'], data['password'])


users = [
        {'username': 'rakib', 'password': '123'},
        {'username': 'rasid', 'password': 'bro'}
        ]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)
"""

# or 


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        


users = [
        {'username': 'rakib', 'password': '123'},
        {'username': 'rasid', 'password': 'bro'}
        ]

#user_object = [User(username=data['username'],password=data['password']) for data in users]

# or you can write in 1 line
user_object = [User(**data) for data in users]


