# Factorial calculation

int = int(input("Enter a non-negative integer: "))

for i in range(int , 1, -1):
    a = i - 1
    int = int * a

print("Factorial is:", int)
