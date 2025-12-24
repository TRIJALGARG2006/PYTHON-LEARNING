#Write a python program using function to convert Celsius to Fahrenheit.

def temp(n):
    a = input("enter your temperature(c or f) :")

    if a == "c" :
        fahrenhiet = (n*1.8) + 32
        print(fahrenhiet)
    else :
        celsuis = (n - 32) / 1.8 
        print(celsuis)

n= int(input("enter your number"))
temp(n)