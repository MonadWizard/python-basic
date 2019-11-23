nums = [1,2,3,4,5,6,7,8,9,0]
# read all element in nums and create new list
new1=[]
for n in nums:
    new1.append(n)
print(new1)
#using comprehentions
new1_1=[n for n in nums]
print(new1_1)

# read all element in nums 'n*n' and create new list

new2 = []
for n in nums:
    new2.append(n*n)
print(new2)

#comprehentions
new2_2 =[n*n for n in nums]
print(new2_2)

# read all element in nums if'n==even' and create new list
#comprehentions
new3_3=[n for n in nums if n%2==0]
print(new3_3)


#(letter ,number) pare.('a,b,c,d)(0,1,2,3) 
new_4 =[]
for letter in 'abcd':
    for num in range(4):
        new_4.append((letter,num))
print(new_4)

#comprehentions
new_4_4 = [(letter,num) for letter in 'abcd' for num in range(4)]
print(new_4_4)