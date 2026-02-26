# #digit seperation

# num = int(input('enter a number:'))
# while(num>0):
#     d = num%10
#     print(d)
#     num=num//10

#     #sum of diigits

num =  int(input('enter a number:'))
sum = 0
while(num>0):
    digit =num%10
    sum += digit
    num = num //10
print('sum of digits is:',sum)



    