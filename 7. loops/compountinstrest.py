p = float(input("enter your amount :"))
r = float(input("interest rate :"))
t = float(input("number of years :"))
n = float(input ("enter the amount of times interest is compounded each year :"))
a = r/100


b = p * (1 + a/n)**(n*t)


print(b)