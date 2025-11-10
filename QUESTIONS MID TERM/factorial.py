while True:
    a = input("Enter a non-negative integer to find its factorial: ")
    
    if a.isdigit():
        number = int(a)
        break
    
    elif a.startswith('-'):
        print("Negative sign detected. Factorial is not defined for negative numbers. Please enter a positive integer.")
    
    else:
        print("Invalid input. Please enter a whole number.")

result = 1
for i in range(1, number + 1):
    result *= i
        
print(f"The factorial of {number} is{result}")
