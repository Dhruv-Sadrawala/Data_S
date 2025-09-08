import numpy as np
import pandas as pd

# Employee Salary Operations
# A company records employee salaries ( ):₹ [30000, 45000, 50000, 35000].
# Tasks:
# • Create a Series with custom index labels: ['E1', 'E2', 'E3', 'E4'].
# • Apply a 10% bonus (element-wise multiplication).
# • Display the updated salary of E2 and E4.

ar = np.array([30000, 45000, 50000, 35000])
s_1 = pd.Series(ar,index=['E1', 'E2', 'E3', 'E4'])

print("-----Series-----")
print(s_1)
print("----------------")

s_1 += (ar*10)/100

print("-----10% Updated Salary-----")
print(s_1)
print("----------------")

print("-----10% Updated Salary of E2 and E4-----")
print("E2",s_1['E2'])
print("E4",s_1['E4'])
print("----------------")