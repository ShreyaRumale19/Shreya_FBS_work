# profit = sp - cp  if sp > cp profit
# loss = cp - sp  if sp < cp loss

sp = int(input('enter selling price:'))
cp = int(input('enter cost price:'))

if(sp>cp ):
    print('profit')
elif(sp<cp):
    print('loss')
else:
    print('No profit no loss')    


