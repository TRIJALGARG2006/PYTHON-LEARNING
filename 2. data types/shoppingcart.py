item = input("what would you like to buy :")
price = float(input("what is the price of your item :"))
quantity = int(input("how many would you like :"))
totalprice = quantity*price
print("the name of your item :" , item)
print("the price of your item :" , price)
print("the quantity of your item :" , quantity)
print(f"your total bill for {item} X {quantity} will be {round(totalprice ,2 ) } rupees")