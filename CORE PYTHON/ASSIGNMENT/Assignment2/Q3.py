# int() removes the decimal part (it does NOT round — it truncates).

# Example:

# int(0.3048) → 0

# int(2.54) → 2

# int(5.99) → 5

# It simply cuts off everything after the decimal point.

# If you take float instead of int, the decimal values will be preserved ✅



# #1 feet = 12 inches 
# 1 inch = 0.0254 m 
# 1 feet = 12 * 0.0254

# #Meters = (F × 0.3048) + (I × 0.0254) 
# # or Total inches = (F × 12) + I
# Meters = Total inches × 0.0254

f = int(input('enter value in feets:'))
i = int(input('enter value in inches:'))

m = int(f*0.3048)+(i*0.0254)
c = int(m*100)
print('Total value in meters is:',m)
print('Total value in centimeters is:',c)


# f = float(input("enter value in feets: "))
# i = float(input("enter value in inches: "))

# m = (f*0.3048) + (i*0.0254)
# c = m * 100

# print("Total value in meters is:", m)
# print("Total value in centimeters is:", c)