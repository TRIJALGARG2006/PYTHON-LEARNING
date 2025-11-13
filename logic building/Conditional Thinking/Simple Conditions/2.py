#Check if a number is even or odd.

b = input("enter a number :")

is_valid_integer = False 
if b.isdigit() :
    is_valid_integer = True


if is_valid_integer:
    b = int(b)
    if b % 2 == 0:
        print("you entered an even number")
    else:
        print("you entered an odd number")

else :
    print("invalid value . pls enter an integer")