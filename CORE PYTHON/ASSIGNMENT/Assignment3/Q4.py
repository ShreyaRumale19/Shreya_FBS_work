# a + b > c
# b + c > a
# a + c > b

# This is called the Triangle Inequality Theorem.
# Sum of any two sides must be greater than the third side.

a = int(input('side a is:'))
b = int(input('side b is:'))
c = int(input('side c is:'))


if(a+b > c and b+c > a and a+c > b):
    print('Triangle is valid')
else:
    print('Triangle is not valid')    