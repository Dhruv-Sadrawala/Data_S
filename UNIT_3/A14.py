import numpy as np
import pandas as pd

# DataFrame Creation from Real Data
# Create a DataFrame for 5 employees with columns: Name, Age, Department.
# Tasks:
# • Display the first 3 rows using .head().
# • Show the shape of the DataFrame.
# • Display the data types of all columns.

data = {
	'Name':["ABC","GHJ","TYI","IKL","OPL"],
	'Age':[12,34,55,67,77],
	'Department':["HR","Sales","Accounts","Support","Manager"]
}

df = pd.DataFrame(data)

print("-------Data Frame-------")
print(df)
print("------------------------")

print("-------First 3 Rows Data Frame-------")
print(df.head(3))
print("------------------------")

print("-------Data Frame Shape-------")
print(df.shape)
print("------------------------")

print("-------Data Frame Data Type-------")
print(df.dtypes)
print("------------------------")