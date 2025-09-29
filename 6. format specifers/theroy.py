# format specifiers| = {value:flags} format a value based on what
# flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator



price1 = 456.2222
price2 = 22222.456
price3 = 93.6178

print(f"price is {price1:.1f}")
print(f"price is {price2:.1f}")
print(f"price is {price3:.1f}")