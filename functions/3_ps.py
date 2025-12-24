
#Write a recursive function to calculate the sum of first n natural numbers.

def fact(n) :
    if n == 0 :
        return 0
    return n+fact(n-1)
num = int(input("enter an number"))
print(fact(num))