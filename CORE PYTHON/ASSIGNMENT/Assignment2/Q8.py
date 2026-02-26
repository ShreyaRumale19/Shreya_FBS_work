#swiping using third variable use temp as third variable


A = int(input('enter number A:'))
B = int(input('enter number B:'))

temp = A
A = B
B = temp

print('Value of A is:',A)
print('value of B is:',B)
