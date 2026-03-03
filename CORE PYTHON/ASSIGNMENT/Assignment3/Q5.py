a = int(input('side a is:'))
b = int(input('side b is:'))
c = int(input('side c is:'))

if (a + b > c and b + c > a and a + c > b):
    print('Triangle is valid')
    
    if a == b and b == c:
        print('It is an Equilateral triangle')
    elif a == b or b == c or a == c:
        print('It is an Isosceles triangle')
    else:
        print('It is a Scalene triangle')

else:
    print('Triangle is not valid')

    #10,10,20 not valid , 10,10,15 is valid