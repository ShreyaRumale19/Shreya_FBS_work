# #to check both values are same or not 

# 1️⃣ Identity Operator → is

# Checks whether two variables point to the same object in memory

# It does NOT compare values

# Operators: is, is not

# Example:
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True  (same memory location)
# print(a is c)  # False (different objects)


# Even though a and c look identical, they are stored in different memory locations, so is returns False.

# 2️⃣ Equality Operator → ==

# Checks whether the values are equal

# It does NOT care about memory location

# Example:
# print(a == c)  # True (values are equal)

# 🔥 Why Do We Need is If == Already Exists?

# Because sometimes we care about:

# ✅ Object identity (same object in memory)

# Not just value.

# Most common example:

# x = None

# if x is None:
#     print("x is None")


# Why not use == None?

# Because:

# None is a singleton object in Python

# Best practice (PEP 8) recommends using is None

# It is faster and safer

# 🧠 Real Difference Summary
# Operator	What it checks	Memory location matters?	Used for
# ==	Value equality	❌ No	Comparing data
# is	Object identity	✅ Yes	Checking same object

x = 10 #Immutable
y = 10
z = 20
li1 = [10,20,30]
li2 = [10,20,30]

#1 is 
print(x is y)

#print(x is z)
print(li1 is li2)
print(id(x))
print(id(y))
print(id(z))
print(id(li1))
print(id(li2))
print(id(li1[0]))
