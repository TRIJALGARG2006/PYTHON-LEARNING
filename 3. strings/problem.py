#username shouldnt be more than 12 characters 
#username cant contain spaces 
#username must not contain digits

a = input("enter your username :")

if len(a) > 12:
    print("your username cant be greater than 12 characters")
elif " " in a:
    print("your username cant contain spaces")
elif not a.isalpha() :
    print("your username cant contain digits")
else:
    print(f"welcome {a}")

