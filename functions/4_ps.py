rows = int(input("Enter a number: "))

for i in range(rows, 0, -1): # i = 5, 4, 3, 2, 1 (Controls the number of digits in the row)
    for j in range(rows, rows - i, -1): # j = 5 down to (rows - i + 1)
        print(j, end="")
    print()