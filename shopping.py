from distutils.ccompiler import show_compilers
from logging import exception
shopping_amount = float(input("Enter the shoping amount:"))
discount_amount = 0
payble_amount = 0

if shopping_amount < 0:
    raise Exception("Enter valid amount ")
elif shopping_amount < 1000:
    discount_amount = shopping_amount * 0
elif shopping_amount < 2000:
    discount_amount = shopping_amount * 0.05
elif shopping_amount < 5000:
    discount_amount = shopping_amount * 0.2
else:
    discount_amount = shopping_amount * 0.5

payble_amount = shopping_amount - discount_amount

print(f"shopping amount:{shopping_amount}")
print(f"dicount amount:{discount_amount}")
print(f"payble amount:{payble_amount}")
