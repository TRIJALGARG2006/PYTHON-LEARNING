operator = input("enter any of the following operation + - * /")
num1= float(input("enter your first number : "))
num2 = float(input("enter your second number :"))

if operator == "+" :
    print(round(num1 + num2 , 3))
elif operator == "-" :
    print(round(num1 - num2 , 3))
elif operator == "*" :
    print(round(num1 * num2 , 3))
elif operator == "/" :
    print(round(num1/num2 , 3))