cart = []
price = []

while True:
    items = input("enter your items (Q to quit): ")
    if items.upper() == "Q":
        break
    else:
        prices = float(input("enter the prices of your items: "))
        cart.append(items)
        price.append(prices)

print("your cart")
total = sum(price)

print(cart)
print(price)
print(total)
        
    