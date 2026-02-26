# # to implement multiple condition where next condition depends on previous condition according to situation 

# #taking example of marrage eligiblity criteria
# we use gender as M/f so for that we are taking here only one is m/f anyone is true other condition will false viseversa
# gender and age we are taking as condition so taking #f,F,Female,female,FEMALE any one from this user will enter or m,male,MALE,Male,M

# we will converting all of(#f,F,Female,female,FEMALE any one from this user will enter or m,male,MALE,Male,M) this in lowercase(f,female or m,male) so it will easy to understand to the system any type from above will enter will converted directly into in the lowercase text 
#     so we using str.lower() function
#     then we will check this f,female or m,male by using membership operator in 

gender = input('enter gender(M\F):')
age = int(input('enter age:'))
if(gender.lower()in['f','female']):
    if(age>=18):
        print('eligible for marriage')
    else:
        print('not eligible for marriage')
if(gender.lower()in['m','male']):
    if(age>=21):
        print('eligible for marriage')
    else:
        print('not eligible for marriage')            
