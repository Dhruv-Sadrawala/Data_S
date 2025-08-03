# 3. Store salaries of 6 employees in an array.
# Options:
# a) Increase salaries by 15% and display updated salaries.
# b) Find the highest and lowest salary.
# c) Calculate the mean salary.

import numpy as np

# emp = np.array([]) 
# for i in range(1,7):
# 	n = int(input("Enter employee salaries:"))
# 	emp = np.append(emp,n)

emp = np.array([15000,30000,25000,20000,12000,21000])

print("------ Employees' Previous Salaries ------")
print(emp)

for i in range(len(emp)):
	hike = (emp[i]*15)/100
	up_sal = emp[i]+hike
	emp[i] = up_sal

print("------ Employees' Updated Salaries ------")
print(emp)

print("------ Minimum and Maximum Salaries ------")
print("Lowest salary:",min(emp))
print("Highest salary:",max(emp))

print("------ Mean Salary ------")
print("Mean Salary:",sum(emp)/len(emp))