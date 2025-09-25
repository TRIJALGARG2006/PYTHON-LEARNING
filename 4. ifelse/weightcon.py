weight = float(input("Enter your weight :"))
unit = input("enter your unit (kg or p ) : ")

if unit == "kg" :
    weight = weight * 2.2
    unit = "pounds"
    print(f"your weight is : {weight} {unit}")
elif unit == "p" :
    weight = weight / 2.2
    unit = "kgs"
    print(f"your weight is : {weight} {unit}")
else :
    print(f"this {unit} is not valid only kg / p ")
