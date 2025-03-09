def compute_discount(price, quantity, discount_rate):
    discount_amount = price * quantity * discount_rate
    discounted_price = (price * quantity) - discount_amount
    return discount_amount, discounted_price

quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
discount_rate = float(input("Enter discount rate (as a decimal): "))

discount_amount, discounted_price = compute_discount(price, quantity, discount_rate)

print(f"Quantity: {quantity}, Price: ${price:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")
