#email slicer program 

b = input("enter your email :")

a = b.index("@")

username = b[:a]
domain = b[a + 1:]

print(f"your username is {username} and your domain is {domain}")
