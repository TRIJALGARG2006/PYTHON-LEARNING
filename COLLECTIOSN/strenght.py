password = input("Enter password: ")

if len(password) < 8:
    print("Weak: Too short (minimum 8 characters)")
if not any(c.isupper() for c in password):
    print("Weak: Needs at least one uppercase letter")
if not any(c.islower() for c in password):
    print("Weak: Needs at least one lowercase letter")
if not any(c.isdigit() for c in password):
    print("Weak: Needs at least one digit")
if not any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
    print("Weak: Needs at least one special character")

if (len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)):
    print("Strong Password!")