# 7. Create roll numbers from 101 to 116 using np.arange().
# Options:
# a) Reshape into 4×4 and print.
# b) Print the first two rows.
# c) Print the last column.

import numpy as np

arr = np.arange(101,117)

print("------ Rearrange in 4X4 ------")
ar_2 = arr.reshape(4,4)
print(ar_2)

print("------ First Two Rows ------")
print(ar_2[:2])

print("------ Last Two Columns ------")
print(ar_2[0:,2:])