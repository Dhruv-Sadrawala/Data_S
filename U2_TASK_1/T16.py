# 6. Create a 1D array showing the number of beds occupied in 7 hospital wards.
# Options:
# a) Find the ward with maximum occupancy.
# b) Replace any value below 5 with 5.
# c) Count wards with occupancy above 20.

import numpy as np

bed = np.random.randint(1,30,size=7)

print("------ Ward Bed List ------")
print(bed)

print("------ Maximum Occupied Ward ------")
print(max(bed))

for i in range(len(bed)):
	if bed[i] <= 5:
		bed[i] = 5

print("------ Adjusted Ward Value ------")
print(bed)


print("------ More than 20 wards ------")
count=0

for i in bed:
	if i >= 20:
		print("Ward:",i)
		count+=1
print(count)