#Write a program to sum a list with 4 numbers

a = []

a1 = int(input("enter first number :"))
a.append(a1)
a2 = int(input("enter second number :"))
a.append(a2)
a3 = int(input("enter third number :"))
a.append(a3)
a4 = int(input("enter forth number :"))
a.append(a4)

print(a)

a.append(sum(a))
print(a)