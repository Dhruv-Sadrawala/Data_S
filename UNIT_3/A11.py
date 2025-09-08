import numpy as np
import pandas as pd

# Create and Analyze Sales Data using Series
# A retail shop records its daily sales (in ) for the first week of January:₹
# [1500, 1800, 2100, 1900, 2500, 3000, 2800]
# Tasks:
# • Create a Pandas Series for these sales with days of the week as index labels.
# • Display the sales on Wednesday using label indexing and on the 5th day using
# integer indexing.
# • Calculate the total and average sales.

ar = np.array([1500, 1800, 2100, 1900, 2500, 3000, 2800])
s_1 = pd.Series(ar,index =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

print("-----Series-----")
print(s_1)
print("----------------")

print("-----Accessing Wednesday Using Label-----")
print(s_1['Wednesday'])
print("----------------")

print("-----Accessing 5th Day Using Integer-----")
print(s_1.iloc[4])
print("----------------")

sum_of = pd.Series(sum(ar))
avg_of = pd.Series(sum_of/len(s_1))
print("-----Total and Average Sales-----")
print("Total Sales: ",sum_of[0])
print("Average Sales: ",avg_of[0])