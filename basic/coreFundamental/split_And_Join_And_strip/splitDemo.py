s = 'this is a string of words'
print(s.split())

print("""
""")

print('That   is also        a              string'.split())

print("""
""")

print(s.split('i'))

print("""
""")


words = s.split()
print(words)

for w in words:
    print(w)


 # rsplit
demo = "this is a fucked up"
rsplitee = demo.rsplit(sep=" ", maxsplit=2)
print(rsplitee)

# lsplit
demo = "this is a fucked up"
lsplitee = demo.split(sep=" ", maxsplit=2)
print(lsplitee)

# splitlines split in \n

demo = "this is a fucked up\nfucking univers"
nsplitee = demo.splitlines()
print(nsplitee)





# test
file = """mtv films election, a high school comedy, is a current example
from there, director steven spielberg wastes no time, taking us into the water on a midnight swim
"""

file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(",")
    print(substring_split)
















