def calculate_discount(price, discount_percent):
  if discount_percent < 20:
    return price
  else:
    new_price = price * (discount_percent/100)
    new_price = price - new_price
    return new_price

enter_price = float(input("Enter price of the commodity: "))
enter_discount = float(input("Enter percentage discount: "))
print('Final Price is: $', int(calculate_discount(enter_price, enter_discount)))

# print(f'Final Price is ${int(calculate_discount(enter_price, enter_discount)!)') anyone to explain to me why this line of code has an error. Was trying to use formatted strings.