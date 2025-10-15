a = input("Enter password ")
b = 0
shitcharc = "!@#$%^&*(),.?:{}|<>"
if len(a) >= 8:
    b += 1
if any(t.isupper() for t in a):
    b += 1
if any(t.islower() for t in a):
    b += 1
if any(t.isdigit() for t in a):
    b += 1
if any(t in shitcharc for t in a):
    b += 1
if b == 5:
    print("Strong pass")
else:
    print(f"Weak passoword password rating is {b}/5")