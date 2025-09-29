p = 0 
r = 0 
t = 0 
n = 0

while p<=0 :
    p = float(input("enter a principal value : "))
    if p<=0:
        print("enter a fucking valid ahh value :")
while r <=0 :
    r = float(input("enter your interest rate "))
    if r<=0:
        print("enter a fucking interest value that is valid ")
while t <=0 :
    t = float(input("enter years :"))
    if t<=0:
        print("do u think time moves negative nigga")
while n <=0 :
    n = float(input("how much does it compound per year :"))
    if n<=0:
        print("does it fucking calculate in negative your braindead")
r = r/100
A = p*(1+r/n)**(n*t)
print(A)


 