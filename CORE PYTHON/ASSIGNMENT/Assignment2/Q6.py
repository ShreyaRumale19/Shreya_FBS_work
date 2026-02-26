# Total Salary=Basic+DA+TA+HRA

B = float(input('Enter Basics amount:'))

da = float(10/100)
ta = float(12/100)
hra = float(15/100)

total_salary = float(B +((da + ta+ hra)*B))
print('Total salary of employee is Rs:',total_salary)