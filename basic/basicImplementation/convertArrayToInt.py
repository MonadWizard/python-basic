li1 = ["2 5 5 8"]

li2 = [1,2,3,4,5,6]
print(li1)

print('[%s]' % ', '.join(map(str,li1)))

print(type(li1), " ", type(li2))

print("""
""")


li3 = "1:2:3:4:5:6"
print(li3)
spl = li3.split(':')
print(spl)

for t in spl:
    print(int(t))



