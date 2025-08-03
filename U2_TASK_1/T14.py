# 4. A department recorded research publications by 4 faculty members for 3 years (2D array).
# Options:
# a) Print the total publications for each faculty.
# b) Find which faculty member has the highest total publications.
# c) Print publications for Year 2 only.

import numpy as np

faculty = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])


totals = []
for row in faculty:
    totals.append(sum(row))
totals = np.array(totals)
print("Total publications for each faculty:", totals)

max_faculty = np.argmax(totals)
print(f"Faculty member with the highest total publications: Faculty {max_faculty + 1}")

year_2_publications = faculty[:, 1]
print("Publications for Year 2:", year_2_publications)
