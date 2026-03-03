<<<<<<< HEAD
# 1.[::-1] means reverse the string

# Python automatically flips the number

num = input("Enter a 3-digit number: ")

reverse = num[::-1]

print("Reversed number is:", reverse)

#2. Reversed=(Units×100)+(Tens×10)+Hundreds

num = int(input("Enter a 3-digit number: "))

u = num % 10
num = num // 10

t = num % 10
num = num // 10

h = num

reverse = (u * 100) + (t * 10) + h

=======
# 1.[::-1] means reverse the string

# Python automatically flips the number

num = input("Enter a 3-digit number: ")

reverse = num[::-1]

print("Reversed number is:", reverse)

#2. Reversed=(Units×100)+(Tens×10)+Hundreds

num = int(input("Enter a 3-digit number: "))

u = num % 10
num = num // 10

t = num % 10
num = num // 10

h = num

reverse = (u * 100) + (t * 10) + h

>>>>>>> b85ef56a08465024fdff20233dd97417f1cd42bc
print("Reversed number is:", reverse)