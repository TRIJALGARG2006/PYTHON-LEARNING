unit = input("is your temperature in fahrenhiet or celsuis (F/C) :")
value = float(input("what is value of your temperature :"))

if unit == "C" :
    value = (value(9/5)) + 32 
    print (f"{value} fahrenhiet")
elif unit == "F" :
    value = (value - 32) * 5/9
    print (f"{value} celsuis")
else :
    print("pls input a correct or a valid unit")

