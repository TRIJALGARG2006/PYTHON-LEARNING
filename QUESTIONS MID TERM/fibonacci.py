num_terms = int(input("How many Fibonacci numbers would you like to see? "))

a, b = 0, 1

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The first {num_terms} numbers of the Fibonacci sequence are:")
    for _ in range(num_terms):
        print(a, end='  ')
        old_a = a
        a = b
        b = old_a + b
    print()

