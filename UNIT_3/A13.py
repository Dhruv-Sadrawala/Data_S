import numpy as np
import pandas as pd

# Student Marks from Dictionary
# A school stores student marks in a dictionary:
# {'Math': 78, 'Science': 82, 'English': 90, 'History': 85}
# Tasks:
# • Convert the dictionary into a Pandas Series.
# • Display all subjects where the score is above 80.
# • Find the average score.

dict_1 = {'Math': 78, 'Science': 82, 'English': 90, 'History': 85}

s_1 = pd.Series(dict_1)

print("-----Series-----")
print(s_1)
print("----------------")

print("-----Marks Above 80 in Series-----")
print(s_1[s_1 > 80])
print("----------------")

print("-----Average Score-----")
print(np.mean(s_1))
print("----------------")