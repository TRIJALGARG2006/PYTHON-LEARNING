#take 3 marks from the user and print whether the student is pass or fail 

a = int(input("enter maths marks :"))
b = int(input("enter physics marks :"))
c = int(input("enter python marks :"))

d = ((a+b+c)/300)*100

if a > 33 :
    print("you have passed in maths")
else :
    print("you havent passed in maths")

if b > 33 :
    print("you have passed in physics")
else :
    print("you havent passed in physics")

if c > 33 :
    print("you have passed in python")
else :
    print("you havent passed in python")

if a>33 and b>33 and c>33 and d>40 :
    print("you have passed")
else :
    print("you have failed")