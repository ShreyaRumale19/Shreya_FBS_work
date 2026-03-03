gender = str(input('Enter gender M/F:'))
age = int(input('Enter age:'))

if(gender.lower()in['f','female']):
    if(age >=18):
        print('eligible for marriage')
    else:
        print('not eligible for marriage')
if(gender.lower()in['m','male']):
    if(age>=21):
        print('eligible for marriage')
    else:
        print('not eligible for marriage')
                        