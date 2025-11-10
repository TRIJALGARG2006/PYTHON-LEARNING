rows = int(input("enter the number of lines you want to print : "))
symbol = input("enter whatever you want to print those lines with ")

for i in range(1,rows+1) :
    for j in range(i) :
        print(symbol , end = " ")
    print()
