# Create a 1D NumPy array for marks obtained by 10 students.
# Options:
# a) Print the array and display dtype, shape, and size.
# b) Find the average mark and highest mark.
# c) Count how many students scored above 75.
import numpy as np

student = np.array([]) 
for i in range(1,11):
	n = int(input("Enter marks:"))
	student = np.append(student,n)

print("------ Data Type, Shape, Size ------")
print("Data Type of [student] array:",student.dtype)
print("Shape of [student] array:",student.shape)
print("Size of [student] array:",student.size)

print("------ Average and Highest Marks ------")
print("Average marks:",sum(student)/len(student))
print("Highest marks:",max(student))

print("------ No. of student scored above 75 ------")

count=0

for i in student:
	if i >= 75:
		print("Marks:",i)
		count+=1

print("Count:",count)