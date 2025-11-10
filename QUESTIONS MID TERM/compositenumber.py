A = int(input("Enter a positive integer: "))
if A <= 1:
    print(f"{A} is neither prime nor composite.")
else:
    for i in range(2, A):
        if A % i == 0:
            print(f"{A} is a composite number.")
            break  
    else:
        print(f"{A} is a prime number.")