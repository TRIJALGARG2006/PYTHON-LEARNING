#Check if a number is divisible by 5 and 3

b = input("enter a number :")

a = False
if b.isdigit() :
    a = True

if a:
    b = int(b)
    if b % 5 == 0 and b % 3 == 0 :
        print("the number is divisible by 5 and 3")
    elif b % 5 == 0 :
        print("this number is divisible by 5")
    elif b % 3 == 0 :
        print("the number is divisible by 3")
    else:
        print("the number you entered is not divisible by 5 and 3")

else:
    print("invalid value! enter a number")

    