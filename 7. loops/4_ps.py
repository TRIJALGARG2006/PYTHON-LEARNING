#5. Write a program to find the sum of first n natural numbers using while loop.

a = int(input("enter an number :"))
b =0
# for i in range(1 , a + 1) :
#     b = b + i

# print(b)
i = 0
while (i<=a):
    b = b + i
    i += 1

print(b)