#Check if a number is divisible by 5

b = input("enter a year :")

a = False
if b.isdigit() :
    a = True

if a:
    b = int(b)
    if b % 4 == 0:
        print(f"{b} is a leap year")
    else:
        print(f"{b} is not a leap year")

else:
    print("invalid value! enter an year")