# 1 2 3 5 8 13 21 34 55 89
a = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
for i in range(a):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

print("Fibonacci sequence up to", a, "terms is printed above.")