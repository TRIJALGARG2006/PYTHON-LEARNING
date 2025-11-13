#write a program to find the greatest of 4 numbers entered by the user 

a = int(input("enter a number 1 :"))
b = int(input("enter a number 2 :"))
c = int(input("enter a number 3 :"))
d = int(input("enter a number 4 :"))


if a>b and a>c and a>d :
    print(f"{a} is the biggest number")
elif b>a and b>c and a>d :
    print(f"{b} is the greatest number")
elif c>a and b<c and c>d :
    print(f"{c} is the greatest number")
else : 
    print(f"{d} is the greatest number" )