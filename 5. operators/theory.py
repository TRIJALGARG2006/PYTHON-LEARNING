#logical operators = used for conditional statement 
 
#and = if there are two or more correct but all should be correct 
#or = if one is correct 
#not = gets it in the opposite 


temp = int(input("enter temperature in celsuis"))
sunny = False

if temp > 0 and temp < 30 :
    print("the temperature is good")
else :
    print("the temperature is bad")

if not sunny :
    print("the weather is cloudy")
else :
    print("the weather is sunny")