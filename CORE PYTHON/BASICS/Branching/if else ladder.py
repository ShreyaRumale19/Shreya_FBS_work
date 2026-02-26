#p for percentage

p = int(input('enter percentage:'))

if(p >=91 and p<=100):
    print('Grade is A')
elif(p >=76 and p<=90):
    print('Grade is B')
elif(p >=61 and p<=75):
    print('Grade is C')
elif(p >=41 and p<=60):
    print('Grade is D')
elif(p >=0 and p<=40):
    print('Grade is Fail')

else:
    print('Invalid Percentage.')