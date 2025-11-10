a = int(input("how many students do u want to eval :"))

marks = []
for i in range(0,a) :
    b = float(input("enter marks of student :"))
    if b > 100 or b < 0:
        print("you have entered a wrong value")
    else:
        marks.append(b)
marks.sort()
c = sum(marks) / len(marks)
print(marks)
print(f"your class avg is {c}")