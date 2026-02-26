num = int(input('How many fibonicci number you want:'))
a = -1
b = 1

i = 0
while(i<num):
    c = a+b
    print(c,end = '')
    a = b
    b = c
    i+=1