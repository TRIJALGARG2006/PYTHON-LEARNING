#print pattern 
rows = int(input("enter a number :"))
symbol = input("what do u want to print in the triangle :")
for i in range(1 , rows+1) :
    for j in range(i) :
        print(symbol , end = " ")
    print(i)

    
