n = int(input('Enter a number:'))
for i in range (2,n):#i = 2,3,4,5,....
    if(n%i==0):
      print('no is not prime:',n)
    break
else:
    print('no is prime:',n)    