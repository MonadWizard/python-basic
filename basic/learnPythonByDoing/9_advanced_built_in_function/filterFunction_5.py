def starts_with_f(friend):
    return friend.startswith('f')

friends = ['friend1','unknown','friend2','friend3','legend']
start_with_f = filter(starts_with_f, friends)       # arg 1: function that returns True/False

print(next(start_with_f))
print(list(start_with_f))
print(list(start_with_f))


print("""
      """)

# or we can do same using lambda function

friendss = ['friend1','unknown','friend2','friend3','legend']
start_with_ff = filter(lambda x : x.startswith('f'), friendss)       # arg 1: function that returns True/False

print(next(start_with_ff))
print(list(start_with_ff))
print(list(start_with_ff))



print("""
      """)


# or we can do same with generator comprehention     It's work faster then other 2 process

friendG = ['friend1','unknown','friend2','friend3','legend']
start_with_fff =(f for f in friendG if f.startswith('f'))       # arg 1: function that returns True/False

print(next(start_with_fff))
print(list(start_with_fff))
print(list(start_with_fff))








