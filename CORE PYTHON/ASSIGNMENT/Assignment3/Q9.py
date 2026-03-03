s1 = int(input('Enter marks of sub1: '))
s2 = int(input('Enter marks of sub2: '))
s3 = int(input('Enter marks of sub3: '))
s4 = int(input('Enter marks of sub4: '))
s5 = int(input('Enter marks of sub5: '))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("First Class")
elif percentage >= 60:
    print("Second Class")
elif percentage >= 50:
    print("Third Class")
elif percentage >= 35:
    print("Pass")
else:
    print("Fail")           
