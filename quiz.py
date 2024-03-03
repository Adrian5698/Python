price = 1000000
credit_access = True
if credit_access:
 down_payment = 0.1 * price
else:
 down_payment = 0.2 * price
#print('Down Payment; $', + int(down_payment))
print(f'Down Payment; ${int(down_payment)}')