total = 0
tax = 0

def compute_total_and_tax(quantity, price):
    global total, tax
    total = quantity * price
    tax = total * 0.07

quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

compute_total_and_tax(quantity, price)

print(f"Total: ${total:.2f}")
print(f"Tax (7%): ${tax:.2f}")
