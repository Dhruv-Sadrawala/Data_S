# 2. Create an array of body temperatures (in °C) of 8 patients.
# Options:
# a) Display the minimum and maximum temperature.
# b) Find the number of patients with temperature above 37.5°C.
# c) Change all temperatures above 39°C to 39°C.

import numpy as np

patient = np.array([]) 
for i in range(1,9):
	n = int(input("Enter temprature in C°:"))
	patient = np.append(patient,n)

print("------ Minimum and Maximum Tempartures ------")
print("Minimum temprature in C°:",min(patient))
print("Maximum temprature in C°:",max(patient))

print("------ No. of patient whos temprature is above 37.5°C ------")

count=0

for i in patient:
	if i >= 37.5:
		print("Tempartures above 37.5°C:",i)
		count+=1

print("Count:",count)

for i in range(len(patient)):
	if patient[i] >= 39:
		patient[i] = -2

print(patient)