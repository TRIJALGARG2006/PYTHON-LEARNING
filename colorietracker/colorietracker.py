print("Daily Calorie Tracker ")

mcolorie = 0
print("Morning")

while True:
    noitemin = input("How many food items did you have? ")
    if noitemin.isdigit() > 0:
        break
    print("enter a number")
num_items = int(noitemin)

for i in range(num_items):
    print(f"Item {i + 1}")
    food = input("Enter food name: ")
    
    while True:
        colorieshi = input(f"Enter calories for {food}: ")
        if colorieshi.isdigit():
            break
        print("enter a num")
        
    mcolorie = mcolorie + int(colorieshi)

ecolorie = 0
print("Evening")

while True:
    noitemin = input("How many food items did you have? ")
    if noitemin.isdigit()> 0:
        break
    print("enter a num")
num_items = int(noitemin)

for i in range(num_items):
    print(f"Item {i + 1}")
    food = input("Enter food name: ")
    
    while True:
        colorieshi = input(f"Enter calories for {food}: ")
        if colorieshi.isdigit():
            break
        print("enter a number")
        
    ecolorie = ecolorie + int(colorieshi)

ncolorie = 0
print("Night")

while True:
    noitemin = input("How many food items did you have? ")
    if noitemin.isdigit() > 0:
        break
    print("enter a num")
num_items = int(noitemin)

for i in range(num_items):
    print(f"Item {i + 1}")
    food = input("Enter food name")
    
    while True:
        colorieshi = input(f"Enter calories for {food}: ")
        if colorieshi.isdigit():
            break
        print("enter a number")
        
    ncolorie = ncolorie + int(colorieshi)

total = mcolorie + ecolorie + ncolorie
print(f"Morning total: {mcolorie} kcal")
print(f"Evening total: {ecolorie} kcal")
print(f"Night total:   {ncolorie} kcal")

print(f"Total calories for the day: {total} kcal")
