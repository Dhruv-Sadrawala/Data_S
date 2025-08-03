# 5 . Store attendance (out of 30) for 12 students.
# Options:
# a) Display students who attended less than 20 days.
# b) Replace attendance below 15 with 15.
# c) Find the average attendance.

import numpy as np

attend = np.random.randint(1,30,size=12)

print("------ Students attendance ------")

print(attend)

print("------ Students with Less than 20 days attendance ------")

for i in range(len(attend)):
	if attend[i]<20:
		print(i)

for i in range(len(attend)):
	if attend[i] <= 15:
		attend[i] = 15

print("------ Adjusted Students with Less than 15 days attendance ------")

print(attend)

print("------ Average Students attendance ------")

print(f"{sum(attend)/len(attend)}")