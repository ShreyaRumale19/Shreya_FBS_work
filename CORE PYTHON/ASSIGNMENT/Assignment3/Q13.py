units = float(input("Enter total electricity units consumed: "))

bill = 0

# First 50 units
if units <= 50:
    bill = units * 0.50

# Next 100 units (51–150)
elif units <= 150:
    bill = (50 * 0.50) + (units - 50) * 0.75

# Next 100 units (151–250)
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20

# Above 250 units
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50

# Add 20% surcharge
surcharge = bill * 0.20
total_bill = bill + surcharge

print("Electricity Bill before surcharge:", bill)
print("Surcharge (20%):", surcharge)
print("Total Electricity Bill:", total_bill)