#greatest of three numbers 

def great(a,b,c) :
    if (a>b) and (a>c):
        print(a)
    elif (b>c) and (b>a) :
        print(b)
    else :
        print(c)

a = int(input("enter an number :"))
b = int(input("enter an number :"))
c = int(input("enter an number :"))

great(a,b,c) 