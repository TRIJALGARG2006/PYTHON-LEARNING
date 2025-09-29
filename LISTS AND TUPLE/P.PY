password = input("Enter password: ")

score = 0
a = [] 


has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)


if len(password) >= 12:
    score += 2
    a.append("Great! Your password is a good length.")
elif len(password) >= 8:
    score += 1
    a.append("Good! Your password meets the minimum length.")
else:
    score += 0
    a.append("Weak: Your password is too short. Aim for at least 8 characters.")


if has_upper:
    score += 1
    a.append("Includes uppercase letters.")
else:
    a.append("Weak: Missing uppercase letters.")

if has_lower:
    score += 1
    a.append("Includes lowercase letters.")
else:
    a.append("Weak: Missing lowercase letters.")

if has_digit:
    score += 1
    a.append("Includes digits.")
else:
    a.append("Missing digits")

if has_special:
    score += 1
    a.append("Includes special characters.")
else:
    a.append("Weak: Missing special characters.")


print("Password Strength Report ")
if score >= 6:
    print("Strong Password ")
    print(f"Score: {score}/6")
elif score >= 4:
    print("Moderate Password ")
    print(f"Score: {score}/6")
else:
    print("Weak Password ")
    print(f"Score: {score}/6")

print("\nSuggestions to improve:")
for shit in a:
    print(f"- {shit}")