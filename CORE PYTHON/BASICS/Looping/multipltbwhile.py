# wap to print multiplication Table

# num = int(input('enetr a number:'))
# i = 1
# while(i<=10):
#     num*i
#     print(num*i)
#     i+=1

# OR

# num = int(input('Enter a number:'))
# i =1
# while(i<=10):
#     print(f'{num}*{i} = {num*i}')
#     i+=1


#3

# num = int(input('enter a number:'))
# for i in range(num,num*10+1,num):
#     print(i)

#4.multiplication table in reverse 

num = int(input('enter a number:'))
for i in range(num*10,num-1,-num):
    print(i)