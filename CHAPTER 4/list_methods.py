friends = ["trijal" , "Harsh" , 6 , 9.5 , "Manas"]

print(friends)

friends.append("TANUSH") #this does insersion of any data type at the end of list 
friends[5] = "Tanush" #this helps in replacing or changing that data type 

friends.append("bhavesh")
friends[6] = 89.567
print(type(friends[6]))

print(friends)

print(friends[1:4]) #this will print 1 to 3 index values same as string 


L1 = [34 , 42 , 22, 41.999 , 8900 , 8899]
L1.sort() # this sorts your whole list from decresing to increasing 
print(L1)
L1.reverse() #this reverses your list
print(L1)
L1.insert(3 , "delhi")
# L1.sort() this will not work if there is a string in your list 
print(L1)
L1.pop(3) #this pops out a value 
print(L1)
print(L1.pop(2))