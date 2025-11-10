D = {}
a = int(input("how many friends do you have"))

for i in range(0, a):
    name = input("enter your name \"my friendo\": ")
    lang = input("enter your favourite language:")
    D.update({name:lang})
print(D)