# num = input("Enter a 3 digit number: ")

# if num == num[::-1]:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")

num = int(input("Enter a 3 digit number: "))

original = num

# Extract digits
hundred = num // 100
ten = (num // 10) % 10
unit = num % 10

# Reverse number
reverse = unit * 100 + ten * 10 + hundred

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")