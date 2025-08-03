# 8. A company has performance scores of 5 employees in 4 skills (2D array).
# Options:
# a) Calculate the mean score per employee.
# b) Find the employee with the highest overall score.
# c) Print scores of skill 2 for all employees

import numpy as np

emp = np.array([[1, 2, 3,6],
                    [4, 5, 6,5],
                    [7, 8, 9,7],
                    [10, 11,18,5]])


mean_scores = np.mean(emp, axis=1)
print("Mean scores per employee:", mean_scores)

highest_score_index = np.argmax(np.sum(emp, axis=1))
highest_score = emp[highest_score_index]
print("Employee with the highest overall score:", highest_score)

skill_2_scores = emp[:, 1]
print("Scores of skill 2 for all employees:", skill_2_scores)