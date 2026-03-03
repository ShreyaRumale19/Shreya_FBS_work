# # If ticket price = 500

# # 30% discount means:
# # You get 30% OFF
# # So you PAY only the remaining 70%


# # Ticket price per person
# ticket_amount = 500

# total_amount = 0

# # Person 1
# p1_age = int(input("Enter age of person 1: "))
# if p1_age < 12:
#     total_amount += ticket_amount * 0.70   # 30% discount
# elif p1_age > 59:
#     total_amount += ticket_amount * 0.50   # 50% discount
# else:
#     total_amount += ticket_amount

# # Person 2
# p2_age = int(input("Enter age of person 2: "))
# if p2_age < 12:
#     total_amount += ticket_amount * 0.70
# elif p2_age > 59:
#     total_amount += ticket_amount * 0.50
# else:
#     total_amount += ticket_amount

# # Repeat same for 3,4,5

# print("Total ticket amount for all 5 people:", total_amount)
ticket_amount = 500
total_amount = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))

    if age < 12:
        total_amount += ticket_amount * 0.70
    elif age > 59:
        total_amount += ticket_amount * 0.50
    else:
        total_amount += ticket_amount

print("Total ticket amount:", total_amount)