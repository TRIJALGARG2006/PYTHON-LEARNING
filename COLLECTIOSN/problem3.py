#Check that a tuple type cannot be changed in python 

a = (234 , 222 ,23 , "Trijal")

a[3] = "harsh"
print(a)
#the output will be an error that tuple does not support item assignment 