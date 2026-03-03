<<<<<<< HEAD
# If the question says:

# “Selling price based on cost price and discount”

# Then logically:
# 👉 They are giving discount on Cost Price, so here CP acts like base price.

cp = float(input('enter cp of book:'))
d = float(input('enter d% of book:')) 

#calculate discount amount 

damount = float(d/100) * cp

sp = float(cp - damount)
=======
# If the question says:

# “Selling price based on cost price and discount”

# Then logically:
# 👉 They are giving discount on Cost Price, so here CP acts like base price.

cp = float(input('enter cp of book:'))
d = float(input('enter d% of book:')) 

#calculate discount amount 

damount = float(d/100) * cp

sp = float(cp - damount)
>>>>>>> b85ef56a08465024fdff20233dd97417f1cd42bc
print('Selling price of book is Rs.:',sp)