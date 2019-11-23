friends = {'f1','f2','f3','f4','f5','f6'}
guests = {'g1','f2','f3','f4','g5','g6'}

guest_lower = {name.lower() for name in guests}

present_friends = {name.capitalize() for name in guests if name in friends}
print(present_friends)
# or
present_friend = {name.capitalize() for name in friends & guests}
print(present_friend) 



# now work with list
names = ['f1','f2','f3','f4']
time_last_seen = [10,15,8,5]

"""
first we convert name & time_last_seen to
{
'f1' : 10,
'f2' : 15,
'f3' : 8,
'f4' : 5
}
"""
friend_last_seen = {names[i] : time_last_seen[i] for i in range(len(names))}
print(friend_last_seen)

friend_last_seen_zip = dict(zip(names, time_last_seen))

print(zip(names, time_last_seen)) #[('f1',10),('f2',15),('f3',8),('f4',5)]

print(friend_last_seen_zip)

print(friend_last_seen)
# same as
print(dict([('fd1',100),('fd2',200),('fd3',652)]))




