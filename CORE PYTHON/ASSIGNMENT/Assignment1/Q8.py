#T= total no of days, Y= no. of yrs , W = no.of weeks , D = no.of days ,R = remaining days

T=int(input('enter Total days:'))
# T = 800
# Y = print(T/365)
# R = print(T%365)

# W = print(R/7)
# D = print(R%7)

# Y = T/365
Y = T//365
R = T%365
W = R/7
D = R%7

print('YEARS:',Y)
print('WEEKSS:',W)
print('DAYS:',D)

