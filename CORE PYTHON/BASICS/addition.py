#Take input 
num1 = int(input('enter number1:')) #int'12'
num2 = int(input('enter number2:'))

#print(num1)
#print(type(num1))

#Perform operation
sum = num1 + num2

#Display Result

print(sum)
print('addition is',sum)  #new parameter can be add using comma 
print('addition of'+str(num1)+ '&' + str(num2) +'is' +str(sum)+'.')  
##it all considered as a one parameter due to concatination of different strings 
print(f'addition of {num1} & {num2} is {sum} .')

