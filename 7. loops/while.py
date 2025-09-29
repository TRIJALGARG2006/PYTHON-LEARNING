#while loop = this loop repeats itself till the user goes to another step


a = input("enter your name:")

while a == "" :
    print("you did not enter your name")
    a = input("enter your name:")

print(f"welcome {a}")