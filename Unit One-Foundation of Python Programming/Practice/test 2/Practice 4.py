print(f"{'product':<10} {'price':<10} {'Discount':<10}")
print(f"{'apple':<10} {'0.99$':<10} {'10%':<10}")
price = 0.99
discount = 10
discount_apple = (f"{price/discount:.2 }")
print(discount_apple)