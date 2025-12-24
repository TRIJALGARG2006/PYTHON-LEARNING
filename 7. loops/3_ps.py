#prime number program 

a = int(input("enter any number :"))

for i in range(2 , a) :
    if a % i == 0 :
        print("number is not prime")
        break
else :
    print("its a prime number")