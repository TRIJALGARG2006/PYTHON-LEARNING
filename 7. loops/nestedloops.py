rows = int(input("enter the number of rows :"))
column = int(input("enter the number of columns :"))
symbol = input("which symbol do u want to print :")

for x in range(rows) :
    for y in range(column) :
        print(symbol , end = " ")
    print()