top_friends = ['Jose', 'Rolf', 'Anna']

for i in range(3):
    print(f'My top {i+1} friend is {top_friends[i]}.')
    
for i, friend in enumerate(top_friends):
    print(f'my top {i+1} friend of top_friends list is {friend}')
    
# enumerate make generator
friend_g = enumerate(top_friends)
k, v = next(friend_g)
print(k)
print(v)



