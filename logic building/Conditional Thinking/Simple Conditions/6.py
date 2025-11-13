#Take two numbers and print the larger one.



a = input("enter first number :")
b = input("enter second number :")
c = False
if a.isdigit() and b.isdigit():
    c = True

if c :
    a = int(a)
    b = int(b)
    if a > b :
        print(f"{a} is bigger than {b}")
    elif b > a :
        print(f"{b} is bigger than {a}")
    else :
        print(f"both {a} and {b} are equal")

else :
    print("invalid values . both values should be numbers")
    