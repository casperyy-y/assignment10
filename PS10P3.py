def compute_commission(sales):
    commission_rate = 0.10 if sales > 100000 else 0.05
    commission = sales * commission_rate
    next_year_target = sales * 1.05
    return commission, next_year_target

last_name = input("Enter salesperson last name: ")
sales = float(input("Enter sales amount: "))

commission, next_year_target = compute_commission(sales)

print(f"Salesperson: {last_name}")
print(f"Commission Earned: ${commission:.2f}")
print(f"Next Year’s Sales Target: ${next_year_target:.2f}")
